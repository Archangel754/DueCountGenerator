from anki.hooks import addHook


from aqt.qt import *
from aqt import mw
import sys
sys.path.append('/Users/marshall/DueCountGenerator/')

# import os
#
# path_to_gen = "/Users/marshall/DueCountGenerator/Generator.py"

#path_to_gen = "python /Users/marshall/DueCountGenerator/Generator.py"
# import os
# os.system(path_to_gen)
#import subprocess
#subprocess.call(['python',path_to_gen])

#import subprocess
#subprocess.Popen(path_to_gen, shell=True)

import Generator
import time

def testing1(param="test"):
	if param != "finalize":
		return
	#import sys
	# sys.stderr.write("Starting\n")
	#path_to_gen = "python /Users/marshall/DueCountGenerator/Generator.py"
	# path_to_gen = "ls"

	#import subprocess
	#subprocess.check_call(path_to_gen, shell=True)
	time.sleep(6)
	Generator.main()
	# sys.stderr.write("\nStopping\n")

addHook("sync", testing1)


# add menu item
action = QAction("Write csv file", mw)

mw.connect(action, SIGNAL("triggered()"), testing1)

mw.form.menuTools.addAction(action)
