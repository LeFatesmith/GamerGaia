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

## Deploying the Bot

To deploy the GamerGaia bot to your Discord channel:

1. **Set Up Your Bot on Discord**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot user to your application.
   - Copy your bot token and paste it into the `config.yml` file under `discord_bot_token`.

2. **Invite Your Bot to Your Server**:
   - Generate an OAuth2 URL for your bot with the necessary permissions, including "Read Messages", "Send Messages", and "Manage Messages".
   - Use this URL to invite the bot to your Discord server.

3. **Run the Bot**:
   - Ensure you have Python installed and all dependencies from `requirements.txt` are installed.
   - Run the bot locally by executing:
     ```bash
     python gamergaia.py
     ```
   - Keep the script running to keep the bot active in your server.

For more details on setting up the bot, refer to the [README.md](README.md) file.
