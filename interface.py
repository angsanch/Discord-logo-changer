import tkinter
import gestor
import functools
import os
import subprocess

def newWindow ():
	window = tkinter.Tk ()
	window.minsize (200, 0)
	return window

def constructCanvas (canvas, contents):
	contents = defaultContents (contents)
	for i in contents:
		if   i ["type"] == "Label":
			tkinter.Label (canvas, text = i["text"]).pack (fill = i ["fill"], expand = i ["expand"], side = i ["side"])
		elif i ["type"] == "Button":
			tkinter.Button (canvas, text = i ["text"], command = i ["command"]).pack (fill = i ["fill"], expand = i ["expand"], side = i ["side"])
		elif i ["type"] == "Canvas":
			newCanvas = tkinter.Canvas (canvas)
			constructCanvas (newCanvas, i ["contents"])
			newCanvas.pack (fill = tkinter.BOTH, expand = True)

def defaultContents (conts):
	for i in conts:
		keys = [j for j in i]
		if not "fill" in keys:
			i ["fill"] = tkinter.BOTH
		if not "expand" in keys:
			i ["expand"] = True
		if not "side" in keys:
			i ["side"] = tkinter.TOP

	return conts

def mainMenu (lastWindow = None):
	if lastWindow != None:
		lastWindow.destroy ()
	window = newWindow ()

	conts = [
		{"type" : "Button", "text" : "Change Logo", "command" : lambda: chooseIcon (window)},
		{"type" : "Button", "text" : "Restore default", "command" : window.destroy},
		{"type" : "Button", "text" : "Convert images to icons", "command" : lambda: resetCanvas (canvas)},
		{"type" : "Button", "text" : "Help", "command" : window.destroy}
	]
	constructCanvas (window, conts)
	
	window.mainloop ()

def chooseIcon (lastWindow):
	lastWindow.destroy ()
	window = newWindow()

	conts = [
		{"type" : "Label", "text" : "Choose your icon"}
	]
	for i in gestor.getNames ():
		conts.append ({"type" : "Canvas", "contents" : [
			{"type" : "Button", "text" : i, "side" : tkinter.LEFT, "expand" : True, "command" : functools.partial (changeIcon, i)},
			{"type" : "Button", "text" : "Preview", "side" : tkinter.LEFT, "expand" : False, "command" : functools.partial (subprocess.run, [os.path.join (os.getenv ("windir"), "System32", "mspaint.exe"), os.path.join ("Icons", i + ".ico")])}
			]})
	conts.append ({"type" : "Label", "text" : ""})
	conts.append ({"type" : "Button", "text" : "Back to main menu", "command" : lambda: mainMenu (window)})

	constructCanvas (window, conts)

	window.mainloop ()

def changeIcon (name):
	pass
	#gestor.callChange (name)