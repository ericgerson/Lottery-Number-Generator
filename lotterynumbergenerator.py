"""

Program: lotterynumbergenerator.py
Author: Eric Gerson 
Date : 3/27/19

Lottery Number Generator

GUI-based python program that will display a label at the top and have 5 number fields in the GUI that will accept the output. 
A command button that when clicked, will generate the 5 random numbers between 1 and 55 and place the numbers in the fields for output

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random

class LotteryNumbers(EasyFrame):
	"""Generates and displays a 5 random numbers for a lottery."""
	
	def __init__(self):
		"""Sets up the window, widgets and data."""
		EasyFrame.__init__(self, title = "Lottery Number Generator", background = "gray", resizable = False)
		
		#Label for the title of the application
		titleFont = Font(family = "Georgia", size = 45, weight = "bold")
		self.a = self.addLabel(text = "Lottery Numbers", row = 0, column = 0, columnspan = 2, foreground = "cyan", font = titleFont, background = "gray")
		
		#Labels for the 5 lottery numbers that will be randomized
		numberFont = Font(family = "Arial Black", size = 20, weight = "bold")
		numberPanel = self.addPanel(row = 1, column = 0, background = "gray")
		
		#number1
		self.number1 = numberPanel.addLabel(text = "", row = 0, column = 0,sticky = "NSEW", background = "Navy", foreground = "Tomato", font = numberFont )
		
		#border - number1
		self.number1["borderwidth"] = 4
		self.number1["relief"] ="groove"
		
		#number2
		self.number2 = numberPanel.addLabel(text = "", row = 0, column = 1, sticky = "NSEW",  background = "Navy",foreground = "Tomato", font = numberFont )
		
		#border - number2
		self.number2["borderwidth"] = 4
		self.number2["relief"] ="groove"
		
		#number3
		self.number3 = numberPanel.addLabel(text = "",row = 0, column = 2,sticky = "NSEW", background = "Navy", foreground = "Tomato", font = numberFont )
		
		#border - number3
		self.number3["borderwidth"] = 4
		self.number3["relief"] ="groove"
		
		#number4
		self.number4 = numberPanel.addLabel(text = "", row = 0, column = 3,sticky = "NSEW",  background = "Navy", foreground = "Tomato", font = numberFont )
		
		#border - number4
		self.number4["borderwidth"] = 4
		self.number4["relief"] ="groove"
		
		#number5
		self.number5 = numberPanel.addLabel(text = "", row = 0, column = 4, sticky = "NSEW",  background = "Navy", foreground = "Gold", font = numberFont )
		
		#border - number5
		self.number5["borderwidth"] = 4
		self.number5["relief"] ="groove"

		# The command button to generate the random lottery numbers
		buttonFont = Font(family = "Arial Black", size = 15)
		self.numbersBtn = self.addButton(text = "Click Here to Display The Winning Numbers", row = 2, column = 0, columnspan = 2, command = self.lotteryGenerator)
		
		#font - button
		self.numbersBtn["font"] = buttonFont
		
		#background /foreground colors - button
		self.numbersBtn["background"] = "Gold"
		self.numbersBtn["foreground"] = "Navy"
		
		#border - button
		self.numbersBtn["borderwidth"] = 3
		self.numbersBtn["relief"] = "raised"
		
	# The event handling method for the button
	def lotteryGenerator(self):
	
		#random number generator
		lottery1 = random.randint(1, 55)
		lottery2 = random.randint(1, 55)
		lottery3 = random.randint(1, 55)
		lottery4 = random.randint(1, 55)
		lottery5 = random.randint(1, 55)
		
		#output the random numbers 
		self.number1["text"] = lottery1
		self.number2["text"] = lottery2
		self.number3["text"] = lottery3
		self.number4["text"] = lottery4
		self.number5["text"] = lottery5
	
def main():
	LotteryNumbers().mainloop()

main()