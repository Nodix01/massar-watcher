# Massar Watcher

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A lightweight Python utility that monitors the Morocco Massar portal and alerts you as soon as it becomes reachable during periods of heavy traffic.


## Screenshot

![Massar Watcher running](screenshots/terminal.png)


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

Clone the repository:

```bash
git clone https://github.com/Nodix01/massar-watcher.git
cd massar-watcher
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Configuration

Edit the configuration values at the top of `watcher.py` to customize:

- Target URL
- Check interval
- Maximum backoff
- Discord webhook (optional)

## Usage

Run the watcher:

```bash
python watcher.py
```

The script will periodically check whether the Massar portal is reachable. Once the website responds successfully, it will:

- Play a notification sound
- Print a message to the console
- Optionally send a Discord webhook notification

## Disclaimer

This project is **not affiliated with Massar or the Moroccan Ministry of National Education.**

It does not log into accounts, bypass authentication, access student information, or retrieve grades. It only checks whether the public portal is reachable and notifies the user when it becomes available.

## Contributing

Bug reports, feature requests, and pull requests are welcome.

## License

This project is licensed under the MIT License.
