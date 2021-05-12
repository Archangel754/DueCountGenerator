#!/usr/bin/env python2.7



def reader():
    import urllib, urllib2, cookielib
    from prefs import username, password
    import os
    from os.path import expanduser

    # get path of home folder
    home = expanduser("~")
    deck_file_name = "anki_decks_page"

    # create tmp directory
    # tmp_dir_path = os.path.join(home,'tmpdcg/')
    # os.mkdir(tmp_dir_path)
    
    web_path = os.path.join(home,'tmpdcg/', deck_file_name)
    # print 'web_path:', web_path
    # set up for cookies 
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    params = urllib.urlencode({'username': username, 'password': password})
    opener.open("https://ankiweb.net/account/login", params)


    decks_page = opener.open("https://ankiweb.net/decks/")
    body = decks_page.read()

    #os.mkdir('~/tmpdcg')
    pf = open(web_path,'w')
    pf.write(body)
    pf.close



    #if __name__ == '__main__':
    #    reader()
