# Telegram Nick Checker

Telegram Nick Checker is a Python-based application that uses the asyncio and configparser libraries to check the availability of usernames on Telegram. It provides a simple and efficient way to check multiple usernames at once, allowing you to find available usernames quickly and easily.

## Features

- Check the availability of multiple usernames on Telegram at once
- Uses asyncio to perform asynchronous requests, allowing for faster processing of large lists of usernames
- Uses configparser to load and manage configuration files, making it easy to customize the application settings

## Requirements

- Python 3.7 or higher
- asyncio 3.4.3 or higher
- configparser 5.0.2 or higher

## Installation

To install Telegram Nick Checker, clone this repository and install the required dependencies using pip:

```
git clone https://github.com/BotYanis/telegram-nick-checker.git
cd telegram-nick-checker
pip install -r requirements.txt
```

## Usage

To use Telegram Nick Checker, create a configuration file called `config.ini` in the project directory and add the following lines:

```ini
[Telegram]
