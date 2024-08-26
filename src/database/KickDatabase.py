from pymongo import MongoClient
from src.config.config import env
from typing import Optional


class KickDatabase:
    def __init__(self) -> None:
        self._config = env()
        self._database_name = 'kickbot'
        self._database = self.run()

    def run(self) -> Optional[MongoClient]:
        try:
            self._database = MongoClient(self._config['database'])
            client = self._database
            print('Database | Connected to the database successfully.')
            return client
        except Exception as e:
            print('Database | Failed to connect:', e)
            return None

    def add(self, content, collection) -> None:
        try:
            collection = self._database[self._database_name][collection]
            result = collection.insert_one(content)
            if result.inserted_id:
                print('Content successfully added!')
            else:
                print('Failed to add content.')
        except Exception as e:
            print('Error adding content:', e)

    def update(self, filter, content, collection) -> None:
        try:
            collection = self._database[self._database_name][collection]
            result = collection.update_one(filter, content)
            if result.modified_count > 0:
                print('Content successfully updated!')
            else:
                print('Failed to update content.')
        except Exception as e:
            print('Error updating content:', e)

    def delete(self, content, collection) -> None:
        try:
            collection = self._database[self._database_name][collection]
            result = collection.delete_one(content)
            if result.deleted_count > 0:
                print('Content successfully deleted!')
            else:
                print('Failed to delete content.')
        except Exception as e:
            print('Error deleted content:', e)

    def find(self, content, collection) -> dict:
        try:
            collection = self._database[self._database_name][collection]
            result = collection.find_one(content)
            if result:
                return {
                    'command': result['command'],
                    'message': result['message']
                }
        except Exception as e:
            print('Error finded content:', e)

    def list(self, prefix) -> str:
        try:
            collection = self._database[self._database_name]['commands']
            all_commands = collection.find({})
            all_commands_list = list(all_commands)

            if len(all_commands_list) >= 1:
                commands_dict = []
                for command in all_commands_list:
                    commands_dict.append(prefix + command['command'])
                return ', '.join(commands_dict)
            else:
                return 'Não possui nenhum comando disponível.'
        except Exception as e:
            print('Error list content:', e)
