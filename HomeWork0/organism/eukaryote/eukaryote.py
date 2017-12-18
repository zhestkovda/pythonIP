from ..organism import Organism
from ..organism import eTypeOrganismNone, eTypeOrganismUnicellular, eTypeOrganismMulticellular

class Eukaryote(Organism):
    type_organism = eTypeOrganismMulticellular

    def __init__(self):
        super().__init__()
