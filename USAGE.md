# GamerGaia Bot Usage Guide

## Overview

**GamerGaia** is a Discord bot that integrates with the Steam API to find common games with friends. This bot uses the prefix `gg` for all its commands.

### Prerequisites

Ensure you have configured your `config.yml` file with the following sensitive data:
- `discord_bot_token`: Your Discord bot token.
- `steam_api_key`: Your Steam API key.

The `config.yml.tmp` provided in the repository serves as a template for creating your `config.yml`.

## Commands

### 1. `gg common_games`

Displays the list of games you have in common with your friends on Steam. By default, it shows the games sorted by the number of friends who own them.

#### Usage:

```
gg common_games <steam_id>
```

- **`<steam_id>`**: Your Steam ID, which is required to fetch your game library and friends list.

#### Optional Arguments:

- **`sort_by`**: The sorting method for the common games. Available options:
  - `game_count` (default): Sort by the number of friends who have the game.
  - `alphabetical`: Sort alphabetically by friend names.

- **`filter_online`**: Filters friends by their online status.
  - `1`: Only show friends who are online.
  - `0`: Only show friends who are offline.

- **`filter_game`**: Filters the games by a specific game name. Provide the game name as a string.

#### Examples:

- **Basic Command**:
  ```
  gg common_games 76561198000000000
  ```
  Fetches the list of common games with friends for the given Steam ID.

- **Sorting by Alphabetical Order**:
  ```
  gg common_games 76561198000000000 alphabetical
  ```

- **Filtering by Online Friends**:
  ```
  gg common_games 76561198000000000 game_count 1
  ```

- **Filtering by Game Name**:
  ```
  gg common_games 76561198000000000 game_count 1 "Apex Legends"
  ```

## Deployment

To deploy the GamerGaia bot:

1. **GitHub Repository**: Push your code to your GitHub repository.
   ```bash
   git init
   git add .
   git commit -m "Initial commit for GamerGaia bot"
   git branch -M main
   git remote add origin https://github.com/LeFatesmith/GamerGaia.git
   git push -u origin main
   ```

2. **Heroku Deployment** (Optional): If you want to host the bot on Heroku, create a `Procfile` with the following content:
   ```
   worker: python gamergaia.py
   ```
   
   Follow the [Heroku deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy your bot.

3. **Environment Variables**: Store sensitive data like your Discord Bot Token and Steam API Key as environment variables. On Heroku, you can set these under "Settings" > "Config Vars".

## References

- **Discord.py Documentation**: [https://discordpy.readthedocs.io/](https://discordpy.readthedocs.io/)
- **Steam API Documentation**: [https://developer.valvesoftware.com/wiki/Steam_Web_API](https://developer.valvesoftware.com/wiki/Steam_Web_API)
