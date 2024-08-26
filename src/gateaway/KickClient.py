from src.services.Kick import Kick
from src.gateaway.KickMessages import KickMessages
from src.database.KickDatabase import KickDatabase


class KickClient:
    def __init__(self, channel):
        self._channelName = channel
        self._KickClient = Kick()
        self._channel = self._KickClient.channel(channel)
        self._client = KickMessages(self._channel, self.message)
        self._database = KickDatabase()

    def message(self, message) -> None:

        prefix = "!"
        messages = message['message'].lower()
        message_content = message['message'].lower().split()

        if not message_content[0].startswith(prefix):
            return

        if len(message_content[0]) > 500:
            return self._KickClient.message(
                self._channelName, 'O seu texto possui mais que 500 digitos.')

        if message_content[0] == prefix + "command":
            command = message_content[1]

            if command == "add":
                command_name = message_content[2]
                command_message = ' '.join(message_content[3:])

                if self._database.find({"command": command_name}, 'commands'):
                    return self._KickClient.message(
                        self._channelName, 'Um comando com o mesmo nome já foi cadastrado no banco de dados.')

                self._database.add(
                    {"command": command_name, "message": command_message}, 'commands')
                return self._KickClient.message(
                    self._channelName, '- Comando adicionado com sucesso.')

            elif command == "edit":
                command_name = message_content[2]
                command_message = ' '.join(message_content[3:])

                filter = {"command": command_name}
                update = {"$set": {"message": command_message}}
                self._database.update(filter, update, 'commands')
                return self._KickClient.message(
                    self._channelName, '- Comando editado com sucesso.')

            elif command == "delete":
                command_name = message_content[2]
                self._database.delete({"command": command_name}, 'commands')
                return self._KickClient.message(
                    self._channelName, '- Comando deletado com sucesso.')

        if messages == f"{prefix}comandos":
            content = self._database.list(prefix)
            return self._KickClient.message(self._channelName, content)

        if message_content[0].startswith(prefix):
            content = self._database.find(
                {"command": message_content[0][1:]}, 'commands')
            
            if message['sender_id'] == 7259604:
                return

            return self._KickClient.message(
                self._channelName, content['message'])

    def run(self):
        self._client.run()
