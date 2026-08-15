# Home Assistant - Energie.be Price Sensors

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)

This custom integration for [Home Assistant](https://www.home-assistant.io/) adds sensors that fetch the current energy prices from [Energie.be](https://energie.be).

> [!IMPORTANT]
> Unofficial integration, built and maintained by [@FabianMeul](https://github.com/FabianMeul). It is not affiliated with, endorsed by, or supported by Energie.be — it simply reads their public tariff page. Please report problems [here](https://github.com/FabianMeul/home-assistant-energie-be/issues) rather than to Energie.be.
>
> Prices are scraped from a web page, so they can break without warning if that page changes. Don't rely on them for billing.

## 📦 Features

- Scrapes the latest **electricity price**, **gas price**, and **injection price**
- Exposes them as sensor entities, grouped under a single **Energie.be** device:

  | Entity | Unit |
  | --- | --- |
  | `sensor.energie_be_electricity_price` | €/kWh |
  | `sensor.energie_be_injection_price` | €/kWh |
  | `sensor.energie_be_gas_price_eur_kwh` | €/kWh |
  | `sensor.energie_be_gas_price_eur_m3` | €/m³ |
  | `sensor.energie_be_gas_conversion_factor` | kWh/m³ |

- Refreshes **once a day** with a single request shared by all sensors, matching the monthly cadence at which the tariff is indexed (a failed fetch retries within 30 minutes rather than waiting for the next day)
- Records long-term statistics, so the prices show up in history and can be used in dashboards, automations, and the Energy panel

### Gas in €/m³

Energie.be quotes gas in c€/kWh, but Belgian meters read m³. The conversion depends on the calorific value of the gas at your reception station (GOS), which [Atrias](https://www.atrias.be/sector-data) publishes officially once a month — it varies slightly per station and drifts month to month.

Pick your station during setup and the integration tracks that value automatically; `sensor.energie_be_gas_conversion_factor` exposes the figure in use, with the station and source month as attributes. If you don't know your GOS, ask your grid operator, or leave it on the Belgian average — every active station currently sits within about 1% of it.

When Atrias can't be reached the €/m³ sensor falls back to that average rather than going unavailable, and the attribute says so.

## 📁 Installation

### HACS

[![Open your Home Assistant instance and open this repository inside HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=FabianMeul&repository=home-assistant-energie-be&category=integration)

Add this repository as a [custom repository](https://www.hacs.xyz/docs/faq/custom_repositories/) in HACS, download it, then restart Home Assistant.

### Manual

Copy the `custom_components/energiebe` directory into your Home Assistant `config/custom_components/` directory, then restart Home Assistant:

```bash
git clone https://github.com/FabianMeul/home-assistant-energie-be.git
cp -r home-assistant-energie-be/custom_components/energiebe /path/to/config/custom_components/
```

## ⚙️ Configuration

Add the integration from **Settings → Devices & Services → Add Integration → Energie.be** and pick your gas reception station (GOS) from the list. You can change it later via **Configure** on the integration card.
