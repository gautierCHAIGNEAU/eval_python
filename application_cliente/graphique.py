import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


class Graphique:
    
    def __init__(self, data):
        self.data = data

    def dessiner(self):

        n_groups = len(self.data['Londres'])


        londres_data = self.data['Londres']

        paris_data = self.data['Paris']

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, londres_data, bar_width,
                        alpha=opacity, color='b', error_kw=error_config,
                        label='Londres')

        rects2 = ax.bar(index + bar_width, paris_data, bar_width,
                        alpha=opacity, color='r', error_kw=error_config,
                        label='Paris')

        ax.set_xlabel('Mois')
        ax.set_ylabel('Température')
        ax.set_title('Températures comparées')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'))
        ax.legend()

        fig.tight_layout()
        plt.show()