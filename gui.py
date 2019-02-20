from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename

def openFile():
	filename = askopenfilename()
	print(filename)
	return filename;

def gui():
	root = Tk()
	root.title("EiT - Maskinlæring, Gruppe 1")

	img = ImageTk.PhotoImage(Image.open("cat.jpg"))

	panel = Label(root, image=img)
	panel.pack()

	button = Button(root, text="hei", width=25, command=openFile)
	button.pack()

	mainloop()

if __name__ == '__main__':
    gui()
