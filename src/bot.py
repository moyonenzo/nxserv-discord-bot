import datetime
import discord
from discord.ext import tasks

from src.server import Server

def format_duration(seconds: float) -> str:
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours}h" if hours > 0 else f"{minutes}m"

class Client(discord.Client):
    async def on_ready(self):
        self.gameserver = Server("51.195.79.106", 27015)
        self.channel = self.get_channel(1455681895588302868)
        self.embed_message = None

        self.update_status.start()

    @tasks.loop(minutes=1)
    async def update_status(self):
        infos = self.gameserver.get_infos()
        activity = discord.Game(f"🔵 {infos.player_count}/{infos.max_players} joueurs")
        await self.change_presence(status=discord.Status.online, activity=activity)

        if self.embed_message is None:
            async for msg in self.channel.history(limit=100):
                if msg.author == self.user and msg.embeds:
                    self.embed_message = msg
                    break

        players_text = ""
        for player in self.gameserver.get_players():
            players_text += f"→ {player.name}\n"

        embed = discord.Embed(color=discord.Color.blue() if infos.player_count > 0 else discord.Color.red())
        embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1037817329611980844/1455670837729562755/images.png?ex=6955929c&is=6954411c&hm=e7570ed6fa8b781102120e7e0361cdd82fc0b46f4e829a576a39963dcf6618db&", name=f"Joueurs en ligne : {infos.player_count}/{infos.max_players}")
        embed.add_field(name="\nJoueurs", value=f"{players_text}\n", inline=True)
        embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/1037817329611980844/1455670837729562755/images.png?ex=6955929c&is=6954411c&hm=e7570ed6fa8b781102120e7e0361cdd82fc0b46f4e829a576a39963dcf6618db&", text="Dernière mise à jour")
        embed.timestamp = datetime.datetime.now(datetime.UTC)  # UTC maintenant

        if self.embed_message:
            await self.embed_message.edit(embed=embed)
        else:
            self.embed_message = await self.channel.send(embed=embed)

    @update_status.before_loop
    async def before_update_status(self):
        await self.wait_until_ready()
