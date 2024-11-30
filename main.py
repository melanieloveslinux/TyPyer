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
		# Vars
		s.background = '#99aaaa'
		s.accuracy = None
		s.textDirectory = "defaultTexts/*" 

		# Window
		s.root = tk.Tk()
		s.root.title("TyPyer - ALPHA")
		s.root.minsize(400, 300)
		s.root.config(bg=s.background)

		s.menu("0")

	def menu(s, crash):
		s.newScreen()

		# Canvas Item Definitions (Frames then Items)
		startButton = tk.Button(s.root, text="Start Game", bg=s.background, command=s.inGame)
		settingsButton = tk.Button(s.root, text="Settings Menu", bg=s.background, command=s.optionMenu)
		quitButton = tk.Button(s.root, text="Quit Game", bg=s.background, command=lambda: s.root.destroy())

		# Canvas Item Placements
		startButton.pack(anchor='s', ipady=5, ipadx=10, expand=True)
		settingsButton.pack(expand=True, ipady=5, ipadx=10)
		quitButton.pack(anchor='n', ipady=5, ipadx=10, expand=True)

		# Conditional Items
		if crash != "0":
			crashLab = tk.Label(s.root, bg=s.background, text=crash)
			crashLab.pack(anchor='n', expand=True)
		if s.accuracy != None:
			accuracyLab = tk.Label(s.root, bg=s.background, text=f"Accuracy:  {s.accuracy}%")
			accuracyLab.pack(anchor='n', expand=True)
			

	def optionMenu(s):
		s.newScreen()

		def getDir():
			s.textDirectory = str(f"{fd.askdirectory()}/*")
		
		# Definitions
		menuButton = tk.Button(s.root, text="Main Menu", bg=s.background, command=lambda: s.menu("0"))
		getDirButton = tk.Button(s.root, text="Select Folder", bg=s.background, command=getDir)
		
		# Placements
		menuButton.pack(anchor='s', expand=True)
		getDirButton.pack(anchor='n', pady=5, expand=True)


	def assessSubmission(s, originalText, userText):
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
				s.assessSubmission(textToType,typingBox.get("1.0","end"))

		# Grab random file from directory
		# TODO Fix selecting folders outside of the TyPyer folder & selecting folders as 'files to open'.
		try:
			txtfiles = glob.glob(s.textDirectory, recursive=True)
			with open(random.choice(txtfiles), 'r') as fi:
				textToType = ''
				fi.seek(0)
				for li in fi:
					textToType += li
		except:
			s.menu(f"Invalid folder choice!  Cannot use the directory:  {s.textDirectory}")
		
		# Definitions
		textDisplay = tk.Label(s.root, text=f"{textToType}", bg=s.background)

		typingBox = tk.Text(s.root, height=10,  bg='#eeeeee')
		typingBox.bind("<Key>", keyFunc)
		
		finishButton = tk.Button(s.root, text="Finish", bg=s.background, command=lambda: s.assessSubmission(textToType,typingBox.get("1.0","end")))

		
		# Placements
		textDisplay.pack(pady=5, anchor='s', expand=True)
		typingBox.pack(padx=50, pady=30, expand=True)
		finishButton.pack(ipady=5, ipadx=10, anchor='n', expand=True)

		typingBox.focus_set() # Bring text box to focus (user convenience)

	# When called, clears all items on the root window.
	def newScreen(s):
		for item in s.root.winfo_children():
			item.destroy()



# Main
typyer = game
typyer().root.mainloop()
