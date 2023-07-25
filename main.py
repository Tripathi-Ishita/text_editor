import os.path
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from emoji import emojize
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
def insert_emoji(emoji):
    selected_emoji = emoji_listbox.get(emoji_listbox.curselection())
    unicode_emoji = emojize(selected_emoji)
    text_box.insert(tk.INSERT, unicode_emoji)


def newFile():
    global file
    window.title("Untitled-Notepad Alpha")
    file=None
    text_box.delete(1.0,END)#1st line k 0th charcater se sab delete
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                   ("Text Documents","*.txt") ])
    if file=="":
        file=None
    else:
        window.title(os.path.basename(file) + "-Notepad Alpha")
        text_box.delete(1.0, END)
        f=open(file,"r")
        text_box.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                   ("Text Documents","*.txt") ])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(text_box.get(1.0,END))
            f.close()
            window.title(os.path.basename(file)+"-Notepad")
    else:
        f = open(file, "w")
        f.write(text_box.get(1.0, END))
        f.close()

def Quit():
    window.destroy()


def cut():
    text_box.event_generate(("<<Cut>>"))
def copy():
    text_box.event_generate(("<<Copy>>"))
def paste():
    text_box.event_generate(("<<Paste>>"))
def about():
    showinfo("NotePad Alpha","NotePad Alpha by Tripathi Ishita (^◕.◕^)")
window = tk.Tk()
window.title("Text Editor")
window.iconbitmap("image/icon4.ico")
text_box = scrolledtext.ScrolledText(window, width=50, height=20)
text_box.configure(font=("Comic Sans MS", 12))
file = None  # no file opened in notepad
MenuBar = Menu(window)
window.config(menu=MenuBar)
FileMenu = Menu(MenuBar, tearoff=0)
# open new file
FileMenu.add_command(label="New", command=newFile)
# open existing file
FileMenu.add_command(label="Open", command=openFile)
# to save current file
FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=Quit)
MenuBar.add_cascade(label="File", menu=FileMenu)

EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

AboutMenu = Menu(MenuBar, tearoff=0)
AboutMenu.add_command(label="About Notepad", command=about)
MenuBar.add_cascade(label="About", menu=AboutMenu)

emoji_button = tk.Button(window, text="Insert Emoji", command=lambda: emoji_window.deiconify())
emoji_button.pack()

emoji_window = Toplevel(window)
emoji_window.title("Select Emoji")
emoji_window.withdraw()  # Hide the emoji window initially

emojis = ["😃", "🌍", "🎉", "❤️", "🐶", "🌻", "🍕","👻","🙂","😂","😥","🤗","😆","😍","😑","😛","😬","🐰","🫰","👏","🫶","🍕","🍔","🍟","🥪"]  # Add more emojis as desired
emoji_listbox = Listbox(emoji_window, width=10, height=5, font=("Arial", 12))
for emoji in emojis:
    emoji_listbox.insert(END, emoji)
emoji_listbox.pack()

select_button = Button(emoji_window, text="Select Emoji", command=lambda: [emoji_window.withdraw(), insert_emoji(emoji_listbox.curselection())])
select_button.pack()

text_box.pack(expand=True,fill=BOTH)
emoji_window.grid()
window.mainloop()

