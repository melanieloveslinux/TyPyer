# Imports
import tkinter as tk
import tkinter.filedialog as fd
import time
import random
import glob



# Classes
# Imported from a stack exchange forum, used to make console messages more readable.
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class game():
	def __init__(s):
		s.root = tk.Tk()
		s.root.title("TyPyer - V0.1")
		s.root.minsize(300, 400)
		s.accuracy = None
		s.textDirectory = "textSamples/*" 
		s.menu("0")

	def menu(s, crash):
		s.newScreen()
		
		# Canvas Item Definitions
		startButton = tk.Button(s.root, text="Start Game", command=s.inGame)
		settingsButton = tk.Button(s.root, text="Settings Menu", command=s.optionMenu)
		quitButton = tk.Button(s.root, text="Quit Game", command=lambda: s.root.destroy())
		
		# Canvas Item Placements
		startButton.pack()
		settingsButton.pack()
		quitButton.pack()

		# Conditional Items
		if crash != "0":
			crashLab = tk.Label(s.root, text=crash)
			crashLab.pack()
		if s.accuracy != None:
			accuracyLab = tk.Label(s.root, text=f"Accuracy:  {s.accuracy}%")
			accuracyLab.pack()
			

	def optionMenu(s):
		s.newScreen()

		def getDir():
			s.textDirectory = str(f"{fd.askdirectory()}/*")
		
		# Definitions
		menuButton = tk.Button(s.root, text="Main Menu", command=lambda: s.menu("0"))
		getDirButton = tk.Button(s.root, text="Select Folder", command=getDir)
		
		# Placements
		menuButton.pack()
		getDirButton.pack()


	def assess(s, originalText, userText):
		correctText = 0
		for x in range(0, min(len(originalText), len(userText))):
			if userText[x] == originalText[x]:
				correctText += 1

		s.accuracy = round((correctText/len(originalText))*100)
		s.menu("0")

	def inGame(s):	
		s.newScreen()
		
		# TODO Fix Ctrl + Backspace not deleting full words
		def keyFunc(event):
			#print(repr(event.char).strip('\n'))
			# User complete text with return key.
			if repr(event.char) == "'\\r'":
				s.assess(textToType,typingBox.get("1.0","end"))

		# Grab random file from directory
		#print(s.textDirectory)
		try:
			txtfiles = glob.glob(s.textDirectory, recursive=True)
			textToType = open(random.choice(txtfiles), 'r').readline()
		except:
			s.menu(bcolors.OKGREEN, f"Invalid folder choice!  Cannot use the directory:  {s.textDirectory}")

		# Definitions
		textDisplay = tk.Label(s.root, text=f"{textToType}")
		typingBox = tk.Text(s.root)
		typingBox.bind("<Key>", keyFunc)
		finishButton = tk.Button(s.root, text="Finish", command=lambda: s.assess(textToType,typingBox.get("1.0","end")))
		
		# Placements
		textDisplay.pack()
		typingBox.pack()
		finishButton.pack()

		typingBox.focus_set() # Focus box (user convenience)

	# When called, clears all items on the root window.
	def newScreen(s):
		for item in s.root.winfo_children():
			item.destroy()


# Main
typyer = game
typyer().root.mainloop()

