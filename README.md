# Massar Watcher

A lightweight Python utility that monitors the Morocco Massar portal and alerts you as soon as it becomes reachable during periods of heavy traffic.

## Why?

Every year during Morocco's baccalaureate results period, the Massar portal receives a huge number of simultaneous visitors. This often makes the website slow or temporarily unavailable, leading many students and parents to spend hours manually refreshing the page.

Massar Watcher automates that process by checking the portal at configurable intervals and notifying you the moment it's available again.

I originally built this as a personal utility and have now made it public so others can use and improve it.

## Features

- Exponential backoff to reduce unnecessary requests
- Configurable polling interval
- Desktop sound notification
- Optional Discord webhook notification
- Lightweight and easy to run
- Cross-platform (Windows, Linux, macOS)

## Installation

```bash
git clone https://github.com/Nodix01/massar-watcher.git

cd massar-watcher

pip install -r requirements.txt
