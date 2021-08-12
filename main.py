import gestor
import command
import os
import shutil

paths = gestor.getPaths ()

if not os.path.exists ("Backup"):
	os.mkdir ("Backup")

if not os.path.exists ("Icons"):
	os.mkdir ("Icons")

if not os.path.exists (os.path.join ("backup", "app.ico")):
	shutil.copy (paths ["ico1"], os.path.join ("backup", "app.ico"))
	print ("Backed up discord icon")

if not os.path.exists (os.path.join ("backup", "Discord.exe")):
	shutil.copy (paths ["exe"], os.path.join ("backup", "Discord.exe"))
	print ("Backed up discord executable")

com = command.Interpreter ()

com.addCommand("getNames", gestor.getNames)
com.addCommand("restore", gestor.callRestore)
com.addCommand("change", gestor.callChange)

print ('Type "listCommands" to see a list of all available commands')
print ('Type "help" before any command to get help')

while True:
	com.call (input ("--- "))