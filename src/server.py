import a2s

class Server:
    def __init__(self, ip: str, port: int):
        self.server_address = (ip, port)
        self.infos = a2s.info(self.server_address)
        self.players = a2s.players(self.server_address)

    def get_infos(self):
        self.infos = a2s.info(self.server_address)
        return self.infos

    def get_players(self):
        self.players = a2s.players(self.server_address)
        return self.players

def format_duration(seconds: float) -> str:
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours}h {minutes}m {secs}s"

server = Server("51.195.79.106", 27015)

player = server.get_players()[0]
print(f"{format_duration(player.duration)} → {player.name}")