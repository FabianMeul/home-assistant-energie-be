import aiohttp
import logging
import requests
from bs4 import BeautifulSoup
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(days=1)

URL = "https://energie.be/"

async def scrape_prices():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, timeout=10) as response:
                html = await response.text()

        soup = BeautifulSoup(html, 'html.parser')
        prices = soup.find_all("div", class_="big-price")
        if len(prices) < 3:
            _LOGGER.warning("Expected at least 3 prices in 'big-price' elements, got %d", len(prices))
            return {}

        def parse_price(el):
            # Convert from c€/kWh to €/kWh by dividing by 100
            return float(el.get_text().strip().replace(",", ".")) / 100

        return {
            "electricity": parse_price(prices[0]),
            "gas": parse_price(prices[1]),
            "injection": parse_price(prices[2])
        }
    except Exception as e:
        _LOGGER.error(f"Failed to scrape Energie.be prices: {e}")
        return {}

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([
        EnergieBeSensor("electricity", "Electricity Price", "€/kWh"),
        EnergieBeSensor("injection", "Injection Price", "€/kWh"),
        EnergieBeSensor("gas", "Gas Price", "€/kWh"),
    ])

class EnergieBeSensor(SensorEntity):
    def __init__(self, key: str, name: str, unit: str):
        self._key = key
        self._attr_name = f"Energie.be {name}"
        self._attr_native_unit_of_measurement = unit
        self._attr_native_value = None
        self._attr_icon = "mdi:cash"

    async def async_added_to_hass(self):
        await self.async_update()

    async def async_update(self):
        prices = await scrape_prices()
        _LOGGER.debug("Fetched prices: %s", prices)
        self._attr_native_value = prices.get(self._key)