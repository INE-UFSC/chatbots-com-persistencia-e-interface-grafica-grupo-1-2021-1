import json
from abc import ABC

class DAO(ABC):
    def __init__(self):
        self.datasource = ''
        self.objectCache = {}

    def __dump(self):
        json.dump(self.objectCache, open(self.datasource, 'wb'))

    def __load(self):
        self.objectCache = json.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.objectCache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.objectCache[key]
        except KeyError:
            print('Chave não encontrada')
            raise KeyError

    def remove(self,key):
        try:
            self.objectCache.pop(key)
            self.__dump()
        except KeyError:
            raise KeyError
    
    def get_all(self):
        return self.objectCache.values()
    
    def import_source(self, path: str):
        self.datasource = path
        with open(self.datasource, 'r') as f:
            data = json.load(f)
        print(data)