from ..organism import Organism
from ..organism import eTypeOrganismNone, eTypeOrganismUnicellular, eTypeOrganismMulticellular

class Bacterium(Organism):
    type_organism = eTypeOrganismUnicellular

    def __init__(self):
        super().__init__()
