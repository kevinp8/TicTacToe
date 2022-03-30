import tkinter as tk
from tkinter import messagebox
import socket

pSocket = 0
whichUser = 0

class BoardClass():
    username = ''
    prevTurnUser = 0
    NumGamesPlayed = 0
    NumWins = 0
    NumTies = 0
    NumLosses = 0

    otherUser = ''
    aSocket = 0
    inclassturn = 0
    marker = 0
    oppMarker = 0

    def __init__(self):
        self.aSocket = pSocket
        self.createBoard()

    #create actual interactive board
    def createBoard(self):
        self.master = tk.Tk()
        self.master.resizable(0,0)
        if whichUser == 1:
            self.master.title('Tic Tac Toe: Player 1')
        else:
            self.master.title('Tic Tac Toe: Player 2')
        
        self.label = tk.Label(text="Username:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        self.label.grid(row=1, column=0)

        self.quitbtn = tk.Button(text="Quit", command=self.quitgame)
        self.quitbtn.grid(row=9, column=1)

        if whichUser == 1:
            self.p1 = tk.StringVar()
            self.player1_name = tk.Entry(textvariable=self.p1, bd=5)
            self.player1_name.grid(row=1, column=1, columnspan=8)
            self.turn = False
            self.submitbutton = tk.Button(text='submit', command=self.updateUser)
            self.submitbutton.grid(row=1, column=10)
            self.message = tk.Label(text="Player 2\'s interface will launch once you submit your username and make your first move.", font='Times 12 bold', bg='white', fg='black', height=1)
            self.message.grid(row=3, column=0, columnspan=12)
            self.buildGrid()
        else:
            self.username = 'player2'
            print('Game will start once Player 1 sends their username.')
            self.otherUser = self.aSocket.recv(1024).decode()
            self.aSocket.send(self.username.encode())
            self.usernameLabel = tk.Label(text=self.username, font='Times 20 bold', fg='black', height=1, width=8)
            self.usernameLabel.grid(row=1, column=1, columnspan=8)
            self.label2 = tk.Label(text="Versus:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
            self.label2.grid(row=2, column=0)
            self.label3 = tk.Label(text=self.otherUser, font='Times 20 bold', fg='black', height=1, width=8)
            self.label3.grid(row=2, column=1, columnspan=8)
            self.turn = False
            self.marker = 'O'
            self.oppMarker = 'X'
            self.message = tk.Label(text=self.otherUser +'\'s move.', font='Times 12 bold', fg='black', height=1)
            self.message.grid(row=3, column=0, columnspan=12)
            self.buildGrid()
            if self.btn1['text'] == ' ':
                self.recvMove()
        
        self.master.mainloop()

    def buildGrid(self):
        self.btn1 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn1)) #1 #lambda: btnClick(button1))
        self.btn1.grid(row=4, column=0)
        self.btn2 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn2)) #2
        self.btn2.grid(row=4, column=1)
        self.btn3 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn3)) #3
        self.btn3.grid(row=4, column=2)
        self.btn4 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn4)) #4
        self.btn4.grid(row=5, column=0)
        self.btn5 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn5)) #5
        self.btn5.grid(row=5, column=1)
        self.btn6 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn6)) #6
        self.btn6.grid(row=5, column=2)
        self.btn7 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn7)) #7
        self.btn7.grid(row=6, column=0)
        self.btn8 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn8)) #8
        self.btn8.grid(row=6, column=1)
        self.btn9 = tk.Button(text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.updateGameBoard(self.btn9)) #9
        self.btn9.grid(row=6, column=2)

    def quitgame(self):
        self.aSocket.send(b'q')
        self.master.destroy()
        self.aSocket.close()
        quit()
    
    def updateUser(self):
        global turn
        self.username = self.p1.get()
        if self.username == '':
            popup = messagebox.showerror(title='Username', message='Please Enter a username.')
        else:
            self.player1_name.grid_forget()
            self.submitbutton.grid_forget()
            self.message.grid_forget()
            self.usernameLabel = tk.Label(text=self.username, font='Times 20 bold', fg='black', height=1, width=8)
            self.usernameLabel.grid(row=1, column=1, columnspan=8)
            self.aSocket.send(self.username.encode())
            self.otherUser = self.aSocket.recv(256).decode()
            self.label2 = tk.Label(text="Versus:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
            self.label2.grid(row=2, column=0)
            self.label3 = tk.Label(text=self.otherUser, font='Times 20 bold', fg='black', height=1, width=8)
            self.label3.grid(row=2, column=1, columnspan=8)
            self.turn = True
            self.marker = 'X'
            self.oppMarker = 'O'
            self.message = tk.Label(text='Your move.', font='Times 12 bold', fg='black', height=1)
            self.message.grid(row=3, column=0, columnspan=12)

    def recvMove(self):
        print('received move')
        oppMove = self.aSocket.recv(1024).decode()
        self.prevTurnUser = self.otherUser
        self.message['text'] = 'Your turn.'
        if oppMove == '1':
            self.btn1['text'] = self.oppMarker
        if oppMove == '2':
            self.btn2['text'] = self.oppMarker
        if oppMove == '3':
            self.btn3['text'] = self.oppMarker
        if oppMove == '4':
            self.btn4['text'] = self.oppMarker
        if oppMove == '5':
            self.btn5['text'] = self.oppMarker
        if oppMove == '6':
            self.btn6['text'] = self.oppMarker
        if oppMove == '7':
            self.btn7['text'] = self.oppMarker
        if oppMove == '8':
            self.btn8['text'] = self.oppMarker
        if oppMove == '9':
            self.btn9['text'] = self.oppMarker
        if oppMove == 'q':
            self.quitgame()
        self.isWinner()
        self.boardIsFull()
        self.turn = True
    
    #keeps track how many games have started
    def updateGamesPlayed(self):
        self.NumGamesPlayed += 1

    #clear the board
    def resetGameBoard(self):
        if whichUser == 1:
            if self.p2.get() == 'y' or self.p2.get() == 'Y':
                self.btn1.configure(state='normal')
                self.btn2.configure(state='normal')
                self.btn3.configure(state='normal')
                self.btn4.configure(state='normal')
                self.btn5.configure(state='normal')
                self.btn6.configure(state='normal')
                self.btn7.configure(state='normal')
                self.btn8.configure(state='normal')
                self.btn9.configure(state='normal')
                self.btn1['text'] = ' '
                self.btn2['text'] = ' '
                self.btn3['text'] = ' '
                self.btn4['text'] = ' '
                self.btn5['text'] = ' '
                self.btn6['text'] = ' '
                self.btn7['text'] = ' '
                self.btn8['text'] = ' '
                self.btn9['text'] = ' '
                self.turn = True
                self.aSocket.send(b'y')
                self.playAgainEntry.grid_forget()
                self.submitbutton2.grid_forget()
                self.messagebottom.grid_forget()
                self.message['text'] = 'Your Turn.'
            elif self.p2.get() == 'n' or self.p2.get() == 'N':
                self.printStats()
                self.aSocket.send(b'n')
            else:
                popup = messagebox.showerror(title='Play Again?', message='Enter y/Y or n/N')
        else:
            self.btn1.configure(state='normal')
            self.btn2.configure(state='normal')
            self.btn3.configure(state='normal')
            self.btn4.configure(state='normal')
            self.btn5.configure(state='normal')
            self.btn6.configure(state='normal')
            self.btn7.configure(state='normal')
            self.btn8.configure(state='normal')
            self.btn9.configure(state='normal')
            self.btn1['text'] = ' '
            self.btn2['text'] = ' '
            self.btn3['text'] = ' '
            self.btn4['text'] = ' '
            self.btn5['text'] = ' '
            self.btn6['text'] = ' '
            self.btn7['text'] = ' '
            self.btn8['text'] = ' '
            self.btn9['text'] = ' '
            self.turn = False
            self.messagebottom.grid_forget()
            self.message['text'] = self.otherUser + '\'s Turn.'
            self.recvMove()

    #updates game board with player's move
    def updateGameBoard(self, button):
        if self.username == '':
            popup = messagebox.showerror(title='Username', message='Please Enter a username.')
        elif self.turn == False:
            pass
        else:
            if button['text'] == 'X' or button['text'] == 'O':
                self.message['text'] = 'Choose another tile.'
            else:
                button['text'] = self.marker
                self.prevTurnUser = self.username
                self.turn = False
                if button == self.btn1:
                    self.aSocket.send(b'1')
                if button == self.btn2:
                    self.aSocket.send(b'2')
                if button == self.btn3:
                    self.aSocket.send(b'3')
                if button == self.btn4:
                    self.aSocket.send(b'4')
                if button == self.btn5:
                    self.aSocket.send(b'5')
                if button == self.btn6:
                    self.aSocket.send(b'6')
                if button == self.btn7:
                    self.aSocket.send(b'7')
                if button == self.btn8:
                    self.aSocket.send(b'8')
                if button == self.btn9:
                    self.aSocket.send(b'9')
                self.isWinner()
                self.boardIsFull()
                if self.winner == False and self.tie == False:
                    self.message['text'] = self.otherUser + '\'s turn.'
                    self.recvMove()


    #checks if latest move resulted in a win
    #Updates wins and losses count
    def isWinner(self):
        #if-else all win situations and last else being tie situation(boardisFull)
        self.winner = False
        if self.btn1['text'] == self.btn2['text'] == self.btn3['text'] == self.marker or self.btn1['text'] == self.btn2['text'] == self.btn3['text'] == self.oppMarker:
            self.winner = True
        if self.btn1['text'] == self.btn4['text'] == self.btn7['text'] == self.marker or self.btn1['text'] == self.btn4['text'] == self.btn7['text'] == self.oppMarker:
            self.winner = True
        if self.btn2['text'] == self.btn5['text'] == self.btn8['text'] == self.marker or self.btn2['text'] == self.btn5['text'] == self.btn8['text'] == self.oppMarker:
            self.winner = True
        if self.btn4['text'] == self.btn5['text'] == self.btn6['text'] == self.marker or self.btn4['text'] == self.btn5['text'] == self.btn6['text'] == self.oppMarker:
            self.winner = True
        if self.btn3['text'] == self.btn6['text'] == self.btn9['text'] == self.marker or self.btn3['text'] == self.btn6['text'] == self.btn9['text'] == self.oppMarker:
            self.winner = True
        if self.btn7['text'] == self.btn8['text'] == self.btn9['text'] == self.marker or self.btn7['text'] == self.btn8['text'] == self.btn9['text'] == self.oppMarker:
            self.winner = True
        if self.btn1['text'] == self.btn5['text'] == self.btn9['text'] == self.marker or self.btn1['text'] == self.btn5['text'] == self.btn9['text'] == self.oppMarker:
            self.winner = True
        if self.btn3['text'] == self.btn5['text'] == self.btn7['text'] == self.marker or self.btn3['text'] == self.btn5['text'] == self.btn7['text'] == self.oppMarker:
            self.winner = True
        if self.winner == True:
            if self.prevTurnUser == self.username:
                self.message['text'] = 'You Win!'
                self.NumWins += 1
            else:
                self.message['text'] = self.prevTurnUser +' Wins!'
                self.NumLosses += 1
            self.btn1.configure(state='disabled')
            self.btn2.configure(state='disabled')
            self.btn3.configure(state='disabled')
            self.btn4.configure(state='disabled')
            self.btn5.configure(state='disabled')
            self.btn6.configure(state='disabled')
            self.btn7.configure(state='disabled')
            self.btn8.configure(state='disabled')
            self.btn9.configure(state='disabled')
            self.updateGamesPlayed()
            self.playAgain()
        else:
            pass

    #checks if board is full/ends in a tie and updates tie count
    def boardIsFull(self):
        self.tie = False
        if self.btn1['text'] == self.btn2['text'] == self.btn3['text'] == self.btn4['text'] == self.btn5['text'] == self.btn6['text'] == self.btn7['text'] == self.btn8['text'] == self.btn9['text'] != ' ':
            self.tie = True
            self.NumTies += 1
            self.message['text'] = 'Tie!'
            self.btn1.configure(state='disabled')
            self.btn2.configure(state='disabled')
            self.btn3.configure(state='disabled')
            self.btn4.configure(state='disabled')
            self.btn5.configure(state='disabled')
            self.btn6.configure(state='disabled')
            self.btn7.configure(state='disabled')
            self.btn8.configure(state='disabled')
            self.btn9.configure(state='disabled')
            self.updateGamesPlayed()
            self.playAgain()
            #display tie message and then play again UI
            
    def playAgain(self):
        if whichUser == 1:
            self.p2 = tk.StringVar()
            self.playAgainEntry = tk.Entry(textvariable=self.p2, bd=5)
            self.playAgainEntry.grid(row=8, column=1)
            self.submitbutton2 = tk.Button(text='submit', command=self.resetGameBoard)
            self.submitbutton2.grid(row=8, column=2)
            self.messagebottom = tk.Label(text="Do You Want To Play Again?.", font='Times 12 bold', bg='white', fg='black', height=1)
            self.messagebottom.grid(row=7, column=1, columnspan=12)
        else:
            self.messagebottom = tk.Label(text="Seeing if " + self.otherUser + ' wants to play again.', font='Times 12 bold', bg='white', fg='black', height=1)
            self.messagebottom.grid(row=7, column=1, columnspan=12)
            self.answer = self.aSocket.recv(1024).decode()
            if self.answer == 'y':
                self.resetGameBoard()
            elif self.answer == 'n':
                self.printStats()

    #prints player's username
    #last person to make a move
    #number of games
    #number of wins
    #number of losses
    #and number of ties
    def printStats(self):
        self.player1_name.grid_forget()
        self.submitbutton.grid_forget()
        self.message.grid_forget()
        self.usernameLabel.grid_forget()
        self.label2.grid_forget()
        self.label3.grid_forget()
        self.btn1.grid_forget()
        self.btn2.grid_forget()
        self.btn3.grid_forget()
        self.btn4.grid_forget()
        self.btn5.grid_forget()
        self.btn6.grid_forget()
        self.btn7.grid_forget()
        self.btn8.grid_forget()
        self.btn9.grid_forget()
        self.playAgainEntry.grid_forget()
        self.submitbutton2.grid_forget()
        self.messagebottom.grid_forget()
        self.usernamelabel = tk.Label(text="username: " + self.username, font='Times 12 bold', bg='white', fg='black', height=1)
        self.usernamelabel.grid(row=0)
        self.lastpersontomakemovelabel = tk.Label(text="Last Move By: " + self.prevTurnUser, font='Times 12 bold', bg='white', fg='black', height=1)
        self.lastpersontomakemovelabel.grid(row=1)
        self.numgameslabel = tk.Label(text="Number of Completed Games: " + str(self.NumGamesPlayed), font='Times 12 bold', bg='white', fg='black', height=1)
        self.numgameslabel.grid(row=2)
        self.numwinslabel = tk.Label(text="Number of Wins: " + str(self.NumWins), font='Times 12 bold', bg='white', fg='black', height=1)
        self.numwinslabel.grid(row=3)
        self.numlosseslabel = tk.Label(text="Number of Losses: " + str(self.NumLosses), font='Times 12 bold', bg='white', fg='black', height=1)
        self.numlosseslabel.grid(row=4)
        self.numtieslabel = tk.Label(text="Number of Ties: " + str(self.NumTies), font='Times 12 bold', bg='white', fg='black', height=1)
        self.numtieslabel.grid(row=5)
        self.quittinglabel = tk.Label(text="Quitting Program in 10 seconds." + str(self.NumTies), font='Times 12 bold', bg='white', fg='black', height=1)
        self.quittinglabel.grid(row=6)
        self.master.after(10000, self.quitgame)
