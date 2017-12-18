from .eukaryote import Eukaryote
from .eukaryote import eTypeOrganismMulticellular

class Animal(Eukaryote):
    type_organism = eTypeOrganismMulticellular

    def __init__(self):
        super().__init__()
