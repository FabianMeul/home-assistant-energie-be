from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.const import Platform

DOMAIN = "energiebe"
PLATFORMS = [Platform.SENSOR]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration manually via configuration.yaml (if desired)."""
    if DOMAIN in config:
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": "import"}
            )
        )
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)