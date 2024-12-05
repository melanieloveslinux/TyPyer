TyPyer
===
Type higher with TyPyer!

(Okay, yes terrible jokes aside)

TyPyer is a typing game made in Python with the Tkinter library.  TyPyer is intended to be fairly simplistic and lightweight.  Any genuine feedback is appreciated!

# Instructions
In the menu you can select 'start', 'options' or 'quit' (which exits the app).  The options menu is rather dry at the moment with only one option, a folder selection.  The start button opens a random text file from the selected folder (there is a default folder if you don't select one ^_^) and you may begin typing, click the 'finish' button when you're done and the app will tell you how accurate you were below the settings button.

When selecting a folder, it should contain files with readable information (like .txt files) and there **must** not be any other folders located in the selected folder.  If TyPyer randomly chooses a folder or can not find any files, it will not start and a debug message will appear below the 'quit' button.

This does mean that yes, you may create your own .txt files to type out!  (Because for how imaganitive I am, I am surely not creative).

# Set-up
To make TyPyer work you simply need Python and Tkinter installed.  Here's a short guide on how to install them depending on your operating system (Windows, or Linux):

Windows:
- [!] There is a start-up sound which plays using mpg123, this program may crash under Windows, if so, you may need to download the program from [their website](https://mpg123.de/download.shtml).
- Python:  Python can be downloaded from the official website, [click here to visit](https://www.python.org/downloads/).
- Tkinter:  Tkinter should work perfectly fine after installing Python!
- Heuristica:  Heuristica, and any font on Windows, can be installed by right clicking its .zip file.  You may get Heuristica's file from [Font Squirrel](https://www.fontsquirrel.com/fonts/euristic)

Linux:
- Python:  Python comes with Linux out of the box, yay!
- Tkinter:  I'm sorry for other Distros but on Arch, run the command `pacman -S tk` then Tkinter should work perfectly fine.
- Heuristica:  (This is just the impractical way I did it) Download the font from [Font Squirrel](https://www.fontsquirrel.com/fonts/euristic), move the file to `/usr/local/share/fonts/ttf/*`, then unzip.
