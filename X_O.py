from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1280x720+0+0")
root.title("PyPower Presents Tic Tac Toe")
root.configure(background = '#ff5c75')
Tops = Frame(root,bg = '#ff5c75',pady = 2, width =1350, height = 100, relief = RIDGE)
Tops.grid(row=0,column=0)

lblTitle = Label(Tops,font=('arial',50,'bold'),text = "PyPower Presents Tic Tac Toe",bd = 21,bg= '#ff984f',fg='black',justify = CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root,bg = 'Powder Blue',pady = 2, width =1350, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame ,bd=10, width =750, height=500, pady=2,padx=10,bg='#ffd9db' ,relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame  =  Frame(MainFrame ,bd=10, width =560, height=500, padx=10,pady=2,bg='#ffd9db',relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame ,bd=10, width =560, height=200, padx=10,pady=2, bg='#ffd9db', relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2  =  Frame(RightFrame ,bd=10, width =560, height=200, padx=10,pady=2, bg='#ffd9db',relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:        
        buttons["text"] = "X"
        buttons.configure(background = "white",fg = 'blue')
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:        
        buttons["text"] = "O"
        buttons.configure(background = "white",fg = 'red')
        click = True
        scorekeeper()

def scorekeeper():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        button1.configure(background = '#ffdd05')
        button2.configure(background = '#ffdd05')
        button3.configure(background = '#ffdd05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background = '#ff6d05')
        button5.configure(background = '#ff6d05')
        button6.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        button7.configure(background = '#ff6d05')
        button8.configure(background = '#ff6d05')
        button9.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        button1.configure(background = '#ff6d05')
        button4.configure(background = '#ff6d05')
        button7.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button5["text"] == "X" and button2["text"] == "X" and button8["text"] == "X"):
        button5.configure(background = '#ff6d05')
        button2.configure(background = '#ff6d05')
        button8.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button6["text"] == "X" and button9["text"] == "X" and button3["text"] == "X"):
        button6.configure(background = '#ff6d05')
        button9.configure(background = '#ff6d05')
        button3.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        button1.configure(background = '#ff6d05')
        button5.configure(background = '#ff6d05')
        button9.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    if (button5["text"] == "X" and button7["text"] == "X" and button3["text"] == "X"):
        button5.configure(background = '#ff6d05')
        button7.configure(background = '#ff6d05')
        button3.configure(background = '#ff6d05')
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player X have won")
        reset()
    # for O
    if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        button1.configure(background = '#90ff0a')
        button2.configure(background = '#90ff0a')
        button3.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        button4.configure(background = '#90ff0a')
        button5.configure(background = '#90ff0a')
        button6.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        button7.configure(background = '#90ff0a')
        button8.configure(background = '#90ff0a')
        button9.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        button1.configure(background = '#90ff0a')
        button4.configure(background = '#90ff0a')
        button7.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button5["text"] == "O" and button2["text"] == "O" and button8["text"] == "O"):
        button5.configure(background = '#90ff0a')
        button2.configure(background = '#90ff0a')
        button8.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button6["text"] == "O" and button9["text"] == "O" and button3["text"] == "O"):
        button9.configure(background = '#90ff0a')
        button6.configure(background = '#90ff0a')
        button3.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        button1.configure(background = '#90ff0a')
        button5.configure(background = '#90ff0a')
        button9.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
    if (button5["text"] == "O" and button7["text"] == "O" and button3["text"] == "O"):
        button3.configure(background = '#90ff0a')
        button5.configure(background = '#90ff0a')
        button7.configure(background = '#90ff0a')
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Pypower Tic Tac Toe","Player O have won")
        reset()
        

def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    
    button1.configure(background = '#a9733b')
    button2.configure(background = '#a9733b')
    button3.configure(background = '#a9733b')
    button4.configure(background = '#a9733b')
    button5.configure(background = '#a9733b')
    button6.configure(background = '#a9733b')
    button7.configure(background = '#a9733b')
    button8.configure(background = '#a9733b')
    button9.configure(background = '#a9733b')

def Newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

lblPlayerX =Label(RightFrame1, font=('arial', 40,'bold'), text="Player X :",padx=2,pady=2, bg="yellow",fg ="black")
lblPlayerX.grid(row=0, column=0,sticky=W)

txtPlayerX=Entry(RightFrame1,font=('arial',40,'bold'),bd=2,fg="black",textvariable= PlayerX, width=14,
justify=LEFT).grid(row=0,column=1)
                 
lblPlayerO =Label(RightFrame1, font=('arial', 40,'bold'), text="Player O :",padx=2,pady=2, bg="yellow",fg = "black")
lblPlayerO.grid(row=1, column=0,sticky=W)

txtPlayerO=Entry(RightFrame1,font=('arial',40,'bold'),bd=2,fg="black",textvariable= PlayerO, width=14,
justify=LEFT).grid(row=1,column=1)

btnReset = Button(RightFrame2, text="Reset", font=('arial', 40,'bold'), height = 1, width=20, bg='#ff984f',command = reset)
btnReset.grid(row=2, column=0,padx = 6,pady =11)

btnNewGame = Button(RightFrame2, text="New Game", font=('arial', 40,'bold'), height = 1, width=20,fg='black', bg='yellow',command = Newgame)
btnNewGame.grid(row=3, column=0,padx = 6, pady =11)

button1 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('arial',30,'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('arial', 30, 'bold'), height = 3, width=8, bg='#a9733b', command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky = S+N+E+W)

root.mainloop()