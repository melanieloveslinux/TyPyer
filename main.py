# Imports
import tkinter as tk
import random
import glob


# Functions



# Classes
class game():
	def __init__(s):
		s.root = tk.Tk()
		s.root.title("TyPyer - V0.1")
		s.root.minsize(300,400)
		s.accuracy = 0
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

		accuracyLab = tk.Label(s.root, text=f"Accuracy:  {s.accuracy}%")
		accuracyLab.pack()

	def optionMenu(s):
		s.newScreen()
		
		# Buttons
		startButton = tk.Button(s.root, text="Main Menu", command=s.menu)
		startButton.pack()


	def assess(s, originalText, userText):
		correctText = 0
		incorrectText= 0

		for x in range(0,max(len(originalText),len(userText))):
			try:
				if userText[x] == originalText[x]:
					correctText+=1
				else:
					incorrectText+=1
			except:
				incorrectText+=1

		# correct:incorrect 24:0
		if incorrectText != 0:
			s.accuracy = round((correctText/len(originalText))*100)
		else:
			s.accuracy = 100
		s.menu()

	def inGame(s):
		s.newScreen()
		

		txtfiles = glob.glob("textSamples/*")
		textToType = open(random.choice(txtfiles), 'r').readline()

		textDisplay = tk.Label(s.root, text=f"{textToType}")
		textDisplay.pack()

		typingBox = tk.Text(s.root)
		typingBox.pack()
		finishButton = tk.Button(s.root, text="Finish", command=lambda: s.assess(textToType,typingBox.get("1.0","end")))
		finishButton.pack()
	

	# When called, clears all items on the root window.
	def newScreen(s):
		for item in s.root.winfo_children():
			item.destroy()


# Main
typyer = game
typyer().root.mainloop()

