#!/usr/bin/env python2.7
# coding: utf-8


def stats_parser():
    import os , time , datetime
    from os.path import expanduser
    home = expanduser("~")
    pg_txt = ''
    stats_file_name = 'anki_stats_test'
    stats_path = os.path.join(home, stats_file_name)
    with open(stats_path, 'r') as stat_file:
        pg_txt = stat_file.read()

    # Get date stats file was modified:
    mod_date = os.path.getmtime(stats_path)
    mod_datetime_struct = datetime.date.fromtimestamp(mod_date)
    date_struct = time.localtime(mod_date)
    mod_date_pretty = time.strftime("%m月%d日まで", date_struct)
    mod_date_day = date_struct[2]

    # make sure stats page is whole collection and for period = 1 month:
    chk_txt = 'Scope: whole collection<br>Period: 1 month'
    if chk_txt not in pg_txt:
        print "Wrong page!!!"
        return
    else:
        # print "Continuing on ahead!"
        pass
    
    # find reps counts:
    beg_index = pg_txt.index('$.plot($("#reps"),')
    beg_index += 19
    end_index = pg_txt.index(', conf);', beg_index)
    counts = pg_txt[beg_index : end_index]

    execstring = 'big_dict = ' + counts
    execstring = execstring.replace('null','"null"')
    execstring = execstring.replace('true','"true"')
    execstring = execstring.replace('false','"false"')
    exec(execstring)

    totals = {}
    for i in range(-29,1):
        totals[str(i)] = 0
        #print i
        # update totals
    for i in big_dict:
        if i["label"] == 'Mature' or i["label"] == 'Young' or i["label"] == 'Learn' or i["label"] == 'Relearn':
            for pair in i['data']:
                #                print pair
                totals[str(pair[0])] += pair[1]

    # creat datapoints dict in json format:
    datapoints = ''
    today = datetime.date.today()

    # for testing:
    #mod_datetime_struct = today - datetime.timedelta(1)
    
    # If fresh stats file today:
    if mod_datetime_struct == today - datetime.timedelta(0):
        for t in range(-29,1):
            mini_dict = '{"title" : "' + str(t) + '" , "value" : "' + str(totals[str(t)]) + '"}, '
            datapoints += (mini_dict)
            
    # If stats file was modded yesterday:
    elif mod_datetime_struct == today - datetime.timedelta(1):
        for t in range(-29,0):
            mini_dict = '{"title" : "' + str(t) + '" , "value" : "' + str(totals[str(t+1)]) + '"}, '
            datapoints += (mini_dict)
        mini_dict = '{"title" : "0" , "value" : "0"}, '
        datapoints += (mini_dict)
    # If stats file not modded today or yesterday:
    else:
        print "This data is old!!!"
        return
        


    # print datapoints

    data_string = datapoints
    big_string = '''{
	"graph" : {
        "font-family" : "courier",
	"title" : "''' + mod_date_pretty + '''",
        "type" : "bar",
	"datasequences" : [
			{
				"color" : "purple",
	       		        "title" : "カードの数",
				"datapoints" : [''' + data_string + '''
      ]	
				
			}
		]
	}
}'''

    #print big_string
    with open('/Users/marshall/Dropbox/anki_stats_page/reps_graph.json','w') as reps_file:
        reps_file.write(big_string)

    # print "Finished reps bar graph"

    
if __name__ == '__main__':
    stats_parser()
       
