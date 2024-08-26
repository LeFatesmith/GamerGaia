import discord
from discord.ext import commands
from steam import WebAPI

# Replace with your Steam API Key
STEAM_API_KEY = 'your_steam_api_key'
# Replace with your Discord Bot Token
DISCORD_BOT_TOKEN = 'your_discord_bot_token'

# Initialize the Steam API client
steam_api = WebAPI(key=STEAM_API_KEY)

# Initialize the Discord bot with the 'gg' abbreviation for commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=['gg ', 'GG '], intents=intents)

# Function to get games owned by a Steam user
def get_steam_games(steam_id):
    response = steam_api.IPlayerService.GetOwnedGames(steamid=steam_id, include_appinfo=True)
    if 'response' in response and 'games' in response['response']:
        return response['response']['games']
    return []

# Function to get a user's friends
def get_friends_list(steam_id):
    response = steam_api.ISteamUser.GetFriendList(steamid=steam_id, relationship='friend')
    if 'friendslist' in response and 'friends' in response['friendslist']:
        return response['friendslist']['friends']
    return []

# Function to get detailed friend info (like online status)
def get_friend_info(steam_id):
    response = steam_api.ISteamUser.GetPlayerSummaries(steamids=steam_id)
    if 'response' in response and 'players' in response['response']:
        return response['response']['players']
    return []

# Function to get games owned by friends
def get_friends_games(steam_id):
    friends = get_friends_list(steam_id)
    friends_games = {}
    for friend in friends:
        friend_steam_id = friend['steamid']
        friends_games[friend_steam_id] = get_steam_games(friend_steam_id)
    return friends_games

# Function to find common games with friends and return detailed information
def find_common_games(steam_id, friends_info):
    user_games = get_steam_games(steam_id)
    user_game_ids = {game['appid']: game for game in user_games}
    
    friends_games = get_friends_games(steam_id)
    common_games = {}

    for friend_id, games in friends_games.items():
        friend_game_ids = {game['appid']: game for game in games}
        common_game_ids = set(user_game_ids.keys()).intersection(friend_game_ids.keys())
        
        if common_game_ids:
            common_games[friend_id] = {
                'games': [user_game_ids[appid] for appid in common_game_ids],
                'friend_info': next((info for info in friends_info if info['steamid'] == friend_id), None)
            }
    
    return common_games

# Function to filter and sort common games based on various criteria
def filter_and_sort_common_games(common_games, sort_by='game_count', filter_by=None):
    if filter_by:
        if 'online_status' in filter_by:
            online_status = filter_by['online_status']
            common_games = {fid: details for fid, details in common_games.items()
                            if details['friend_info'] and details['friend_info']['personastate'] == online_status}
        if 'game_name' in filter_by:
            game_name = filter_by['game_name'].lower()
            common_games = {fid: details for fid, details in common_games.items()
                            if any(game_name in game['name'].lower() for game in details['games'])}

    if sort_by == 'game_count':
        sorted_common_games = sorted(common_games.items(), key=lambda x: len(x[1]['games']), reverse=True)
    elif sort_by == 'alphabetical':
        sorted_common_games = sorted(common_games.items(), key=lambda x: x[1]['friend_info']['personaname'] if x[1]['friend_info'] else '')
    else:
        sorted_common_games = list(common_games.items())
    
    return sorted_common_games

# Discord command to display common games
@bot.command(name='common_games')
async def common_games(ctx, steam_id: str, sort_by: str = 'game_count', filter_online: str = None, filter_game: str = None):
    # Get IDs of channel members
    channel_members = [member.id for member in ctx.channel.members if not member.bot]
    
    # Get friend info
    friends_info = get_friend_info(','.join(str(fid) for fid in channel_members))
    
    # Fetch common games
    common_games = find_common_games(steam_id, friends_info)
    
    # Apply filters and sorting
    filters = {}
    if filter_online:
        filters['online_status'] = int(filter_online)
    if filter_game:
        filters['game_name'] = filter_game
    
    sorted_common_games = filter_and_sort_common_games(common_games, sort_by=sort_by, filter_by=filters)
    
    if not sorted_common_games:
        await ctx.send("No common games found with the specified criteria.")
        return
    
    # Construct the response message
    message = "Games you have in common with your friends in this channel:
"
    for friend_id, details in sorted_common_games:
        friend_info = details['friend_info']
        if friend_info:
            friend_name = friend_info['personaname']
            status = "Online" if friend_info['personastate'] else "Offline"
            games = ', '.join([game['name'] for game in details['games']])
            message += f"**{friend_name}** ({status}): {games}
"
    
    await ctx.send(message)

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
