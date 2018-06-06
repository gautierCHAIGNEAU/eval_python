import json
from graphique import Graphique
from donnees import getDonnees

data =  json.loads(getDonnees())
graph = Graphique(data)
graph.dessiner()

