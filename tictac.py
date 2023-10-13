from tkinter import*
import random

def next(row,column):
    global player
    if buttons[row][column]['text']=="" and winner() is False:
        if player == players[0]:
            
            buttons[row][column]['text'] = player
            if winner() is False :
                player = players[1]
                label.config(text=(players[1]+"  turn"))
            elif winner() is True:
                label.config(text=(players[0]+"  wins"))
            elif winner() == "Tie":
                label.config(text=("Tie!!!"))

        else:
                        
            buttons[row][column]['text'] = player
            if winner() is False :
                player = players[0]
                label.config(text=(players[0]+"  turn"))
            elif winner() is True:
                label.config(text=(players[1]+"  wins"))
            elif winner() == "Tie":
                label.config(text=("Tie!!!"))

def winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']== buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']== buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text']== buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text']== buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif emptySpace() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="pink")
        return "Tie!!!"
    
    else:
        return False
   
def emptySpace():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0 :
        return False
    else :
        return True

def newGame():
    global player
    player = random.choice(players)
    label.config(text=player+"  turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="black")

window=Tk()
window.title("TIic Tac Toe")
players=["X","0"]
player=random.choice(players)
buttons =[[0,0,0],
          [0,0,0],
          [0,0,0]]
label=Label(text=player + "  turn",font=('Poor Richard',40),background="black",foreground="cyan")
label.pack(side="top")

reset=Button(text="restart",font=('Poor Richard',20),background="black",foreground="red2",command=newGame)
reset.pack(side="top")

frame=Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):

        buttons[row][column]=Button(frame,text="",font=('Poor Richard',20),background="black",foreground="light cyan",width=5,height=2,command=lambda row=row,column=column:next(row,column))
        buttons[row][column].grid(row=row,column=column)
window.mainloop()
