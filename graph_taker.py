from anki.hooks import wrap
from anki.stats import CollectionStats
import sys, os
from os.path import expanduser


def myReport(self):
    ### write txt to a file(this should be deck stats in html?
    #my_info = txt
    home = expanduser("~")
    graph_path = os.path.join(home,'anki_stats_test')
    # with open(graph_path, 'w') as the_file:
    #     the_file.write(my_info)

    # test file writing capabilities
    with open(graph_path, 'w') as the_file:
        the_file.write('testing')



CollectionStats.report = wrap(CollectionStats.report, myReport)
