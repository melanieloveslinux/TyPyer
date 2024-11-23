# Imports
import tkinter as tk
import random
import glob


# Functions



# Classes
class game():
	def __init__(s):
		s.root = tk.Tk()	
		s.menu()

	def menu(s):
		s.newScreen()
		
		# Buttons
		startButton = tk.Button(s.root, text="Start Game", command=s.inGame)
		startButton.pack()

		settingsButton = tk.Button(s.root, text="Settings Menu", command=s.optionMenu)
		settingsButton.pack()

		quitButton = tk.Button(s.root, text="Quit Game", command=lambda: s.root.destroy())
		quitButton.pack()

	def optionMenu(s):
		s.newScreen()
		
		# Buttons
		startButton = tk.Button(s.root, text="Main Menu", command=s.menu)
		startButton.pack()



	def inGame(s):
		s.newScreen()
		
		txtfiles = glob.glob("textSamples/*")
		textToType = open(random.choice(txtfiles), 'r').readline()

		textDisplay = tk.Label(s.root, text=f"{textToType}")
		textDisplay.pack()

		typingBox = tk.Text(s.root)
		typingBox.pack()
		
		finishButton = tk.Button(s.root, text="Finish", command=s.menu)
		finishButton.pack()
	
	# When called, clears all items on the root window.
	def newScreen(s):
		for item in s.root.winfo_children():
			item.destroy()


# Main
typyer = game
typyer().root.mainloop()

