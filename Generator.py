#!/usr/bin/env python2.7
import sys
#sys.stderr.write("start gen")
def main():
    #print "I'm in!"
    #sys.stderr.write("start gen main")

    import os
    from os.path import expanduser

    # create directory 'tmpdcg' in user's home folder
    home = expanduser("~")
    #deck_file_name = "anki_decks_page"
    #create tmp directory
    tmp_dir_path = os.path.join(home,'tmpdcg/')
    if not os.path.exists(tmp_dir_path):
        os.mkdir(tmp_dir_path)

    import anki_web_reader
    import anki_decks_parser
    #print "done importing"

    anki_web_reader.reader()
    anki_decks_parser.parser()

    #web_path = os.path.join(home,'tmpdcg/', deck_file_name)
    # remove html file and tmpdir
    #os.remove(web_path)
    #if os.path.exists(tmp_dir_path):
    #    os.rmdir(tmp_dir_path)
    #print "Done generating due counts."
    
    
if __name__ == '__main__':
    # sys.exit(2)
    main()
    # sys.exit(0)
    
