# start again :)
from eolib.data import EoReader
from eolib import Emf

class MapLoader:
    def __init__(self):
        self.map_file_type = None

    def load_emf(self, file_path):
        # basically we're trying to open a binary file and read it via the eolib libary
        with open(file_path, 'rb') as f:
            data = f.read()

        reader = EoReader(data)
        self.map_file = Emf.deserialize(reader)
        
        print(f'name of the map {self.map_file.name} amount of npcs {self.map_file.npcs}')

