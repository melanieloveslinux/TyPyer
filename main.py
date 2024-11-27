# Imports
import tkinter as tk
import tkinter.filedialog as fd
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
		s.accuracy = 0
		s.textDirectory = "textSamples/*" 
		s.menu()

	def menu(s):
		s.newScreen()
		
		# Canvas Item Definitions
		startButton = tk.Button(s.root, text="Start Game", command=s.inGame)
		settingsButton = tk.Button(s.root, text="Settings Menu", command=s.optionMenu)
		quitButton = tk.Button(s.root, text="Quit Game", command=lambda: s.root.destroy())
		accuracyLab = tk.Label(s.root, text=f"Accuracy:  {s.accuracy}%")
		
		# Canvas Item Placements
		startButton.pack()
		settingsButton.pack()
		quitButton.pack()
		accuracyLab.pack()

	def optionMenu(s):
		s.newScreen()

		def getDir():
			s.textDirectory = str(f"{fd.askdirectory()}/*")
		
		# Definitions
		menuButton = tk.Button(s.root, text="Main Menu", command=s.menu)
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
		s.menu()

	def inGame(s):
		s.newScreen()
		
		# Grab random file from directory
		print(s.textDirectory)
		txtfiles = glob.glob(s.textDirectory, recursive=True)
		print(txtfiles)
		print(random.choice(txtfiles))
		textToType = open(random.choice(txtfiles), 'r').readline()

		# Definitions
		textDisplay = tk.Label(s.root, text=f"{textToType}")
		typingBox = tk.Text(s.root)
		finishButton = tk.Button(s.root, text="Finish", command=lambda: s.assess(textToType,typingBox.get("1.0","end")))
		
		# Placements
		textDisplay.pack()
		typingBox.pack()
		finishButton.pack()


	# When called, clears all items on the root window.
	def newScreen(s):
		for item in s.root.winfo_children():
			item.destroy()


# Main
typyer = game
typyer().root.mainloop()

