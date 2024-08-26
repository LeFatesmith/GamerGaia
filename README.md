# GamerGaia Bot Setup Guide

Welcome to the **GamerGaia** Discord bot setup guide. This bot integrates with the Steam API to find common games with friends and uses the abbreviation **gg** for all bot commands.

## Prerequisites

Ensure you have the following before starting:

- **Python 3.8+**: Install Python from [here](https://www.python.org/downloads/).
- **Discord Bot Token**: Obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
- **Steam API Key**: Get your Steam API key from [Steam API Key Management](https://steamcommunity.com/dev/apikey).
- **GitHub Account**: To host the repository.

## Bot Setup

For more details on setting up the bot, refer to the [USAGE.md](USAGE.md) file.

### Folder Structure

```
GamerGaia/
│
├── README.md
├── requirements.txt
├── gamergaia.py
├── LICENSE
├── config.yml.tmp
└── .gitignore
```

## Install Required Libraries

Add the following libraries to `requirements.txt`:

```
discord.py
steam
```

Install the libraries with:

```bash
pip install -r requirements.txt
```

## GamerGaia Bot Implementation

Create the main bot script, `gamergaia.py`.
