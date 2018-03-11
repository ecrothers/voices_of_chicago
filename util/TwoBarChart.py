# Simple bar graph

import numpy as np
import matplotlib.pyplot as plt

def draw(men, women):
    topval = max(men, women)
    ind = np.arange(2)
    width = 0.8

    rects = plt.bar(ind, [men, women], width, align='center', color=['#bf8040','#71da71'])
    ax = plt.gca()

    # add some text for labels, title and axes ticks
    ax.set_ylim([0,topval + (topval*0.15)]) # 15% buffer
    ax.set_ylabel('Words')
    ax.set_title('Spoken words by gender')
    ax.set_xticks(ind)
    ax.set_xticklabels(['Men', 'Women'])

    plt.legend(rects, ('Men', 'Women'))

    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects)

    plt.show()

