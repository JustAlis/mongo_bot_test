from dataclasses import dataclass

@dataclass
class conf:
    mongo_database:str = ''
    mongo_collection: str = ''
    mongo_connection_str: str = ''
    token: str = ''