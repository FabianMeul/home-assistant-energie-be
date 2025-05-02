# Home Assistant - Energie.be Price Sensors

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)

This custom integration for [Home Assistant](https://www.home-assistant.io/) adds sensors that fetch the current energy prices from [Energie.be](https://energie.be).

## 📦 Features

- Scrapes the latest **electricity price**, **gas price**, and **injection price**
- Exposes them as sensor entities in Home Assistant:
  - `sensor.energie_be_electricity_price`
  - `sensor.energie_be_gas_kwh_price`
  - `sensor.energie_be_gas_m3_price`
  - `sensor.energie_be_injection_price`
- Updates **once per day**
- Can be used in dashboards, automations, and the Energy panel

## 📁 Installation

### Manual

```bash
git clone https://github.com/@FabianMeul/home-assistant-energie-be.git custom_components/energiebe
```
