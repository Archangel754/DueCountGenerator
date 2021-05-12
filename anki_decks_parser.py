#!/usr/bin/env python2.7

### Parses Anki decks page and returns list of tuples with names of decks with cards due and due counts.

def parser():
    import csv
    import os
    from os.path import expanduser
    import prefs

    csvloc = prefs.csv_file_loc

    # get path of page file
    home = expanduser("~")
    deck_file_name = "anki_decks_page"
    web_path = os.path.join(home,'tmpdcg/', deck_file_name)

    # read page source from ankiweb decks page into f
    deckfile = open(web_path, 'r')
    decks = []
    newdecks = []
    newdecks.append(prefs.column_widths)
    f = deckfile.readlines()
    deckfile.close()


    # find and return locations of decks with cards due
    for i , line in enumerate(f):
        if "<font color='#007700'>" in line:
            #print f[i-3]
            #print f[i]
            decks.append([f[i-3],f[i]])

    # print 'decks:', decks
    # Strip tuples to just deck names and due counts
    for t in decks:
        # strip deck name
        ind = t[0].find('</')
        deck_name = t[0][0:ind]
        # strip due count
        ind_beg = t[1].find("'#007700'>") + 10
        ind_end = t[1].find('</fon')
        due_count = t[1][ind_beg:ind_end]
        newdecks.append([deck_name,due_count])



    # next two lines: no new decks (for testing)
    # decks = []
    # newdecks = [['90%','10%']]

    # add line with total or finished message to newdecks
    if not decks:
        newdecks.append([prefs.finished_msg , ''])
    else: # if there are decks with cards due
        rev_sum = 0
        for i in range(1,len(newdecks)):
            rev_sum += int(newdecks[i][1])
        newdecks.append(['Total Reviews Due:' , rev_sum])
            
        
    # write due counts to csv file:
    with open(csvloc , "w") as the_file:
        csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
        writer = csv.writer(the_file, dialect="custom")
        for tup in newdecks:
            writer.writerow(tup)

if __name__ == '__main__':
    parser()
