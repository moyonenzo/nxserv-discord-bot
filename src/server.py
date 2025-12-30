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
