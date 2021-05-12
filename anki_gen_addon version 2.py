from anki.hooks import addHook
import os

path_to_gen = "/Users/marshall/DueCountGenerator/Generator.py"

def onSyncFin():
	os.system(path_to_gen)

addHook("quit", onSyncFin)
