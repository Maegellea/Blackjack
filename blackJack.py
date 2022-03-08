import random
class Blackjack:
    def __init__(self):
        self.number = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.shape = ["♠","♦","♣","♥"]
        self.deck =  []
        self.playerCards = []
        self.playerTotal = 0
        self.playerAces = 0
        self.computerCards = []
        self.computerTotal = 0
        self.computerAces = 0
        self.createDeck()
    def createDeck(self):
        for i in self.number:
            pile = ""
            for y in self.shape:
                pile = i + y
                self.deck.append(pile)
        random.shuffle(self.deck)
        self.starterDeck()
        
    def starterDeck(self):
        self.playerCards.append(self.deck[len(self.deck)-1])
        self.deck.pop()
        self.playerCards.append(self.deck[len(self.deck)-1])
        self.deck.pop()
        
        self.computerCards.append(self.deck[len(self.deck)-1])
        self.deck.pop()
        self.computerCards.append(self.deck[len(self.deck)-1])
        self.deck.pop()
        
        for card in self.playerCards:
            x = card[0]           
            if (x == "J") or (x == "Q") or (x == "K") or (x == "1"):
                self.playerTotal += 10
            elif x == "A":
                self.playerTotal += 11
                self.playerAces += 1
            else:                
                self.playerTotal += int(x)
        
        for card in self.computerCards:
            x = card[0]
            if x == "J" or x == "Q" or x == "K" or x == "1":
                self.computerTotal += 10
            elif x == "A":
                self.computerTotal += 11
                self.computerAces += 1
            else:
                self.computerTotal += int(x)
        self.startGame()

    def startGame(self):
        print("Your cards:",self.playerCards)
        print("Total:",self.playerTotal)
        print("Computer cards:",[self.computerCards[0],"Hidden Card"])
        while True:
            arc = input("Hit or stand: ")
            if self.playerTotal <= 21:
                if arc == "hit":
                    self.hitCard("player")
                    if self.playerTotal > 21:
                        if self.playerAces > 0:
                            self.playerTotal -= 10
                            self.playerAces -= 1 
                        else:
                            print("You lost!\nYour cards:", self.playerCards,"\nYour total:",self.playerTotal)
                            break
                    print("Your cards:",self.playerCards)
                    print("Total:",self.playerTotal)
                elif arc == "stand":
                    self.startComputer()
                    break
                

    def hitCard(self,param):
        if param == "player":
            self.playerCards.append(self.deck[len(self.deck)-1])
            self.deck.pop()
            self.calculateTotal("player")
        elif param == "computer":
            self.computerCards.append(self.deck[len(self.deck)-1])
            self.deck.pop()
            self.calculateTotal("computer")

    def checkAces(self):
        while self.playerTotal > 21:
            if self.playerAces > 0:
                self.playerTotal -= 10
                self.playerAces -= 1

    def calculateTotal(self,param):
        if param == "player":
            x = self.playerCards[-1][0]
            if (x == "J") or (x == "Q") or (x == "K") or (x == "1"):
                    self.playerTotal += 10
            elif x == "A":
                self.playerTotal += 11
                self.playerAces += 1
            else:               
                self.playerTotal += int(x)
        elif param == "computer":
            x = self.computerCards[-1][0]
            if (x == "J") or (x == "Q") or (x == "K") or (x == "1"):
                self.computerTotal += 10
            elif x == "A":
                self.computerTotal += 11
                self.computerAces += 1
            else:
                self.computerTotal += int(x)

    def startComputer(self):
        while True:
            if self.computerTotal > 21:
                if self.computerAces > 0:
                    self.computerTotal -= 10
                    self.computerAces -= 1
                    self.hitCard("computer")
                else:
                    print("You win!\nYour cards:", self.playerCards,self.playerTotal,"\nComputer cards:",self.computerCards,self.computerTotal)
                    break
            elif self.computerTotal < 21:
                if self.computerTotal >= self.playerTotal:
                    print("You Lost!\nYour cards:", self.playerCards,self.playerTotal,"\nComputer cards:",self.computerCards,self.computerTotal)
                    break
                else:
                    self.hitCard("computer")
            elif self.computerTotal == 21:
                print("You Lost!\nYour cards:", self.playerCards,self.playerTotal,"\nComputer cards:",self.computerCards,self.computerTotal)
                break
           

x = 1
while True:
    val = input("1-Play\n2-How to play\n3-Rules\n4-Exit\n: ")
    if val == "1":
        while True:
            print("|"+f"Round {x}".center(70,"-")+"|")
            x += 1
            Blackjack()
            
            
    elif val == "2":
        print("Blackjack is a game that the player draws a card until total value of player reaches 21. \nEvery card has a number value. For example value of three of clubs is three.\nIf the player's total value is greater than the computer's and if it is smaller than 21 or equal to 21, player will win.However, there is a value limit which is '21'.\nIf the player draws a card and if the total value of the player is greater than 21, player loses.\nThere is one exceptional card which named 'A' (ace).\nYou are able to change the value of this card. You can take the value as 1 or 11.\nIf the total value of your cards is greater than 21, then you can take the value of the ace as '1'\nOtherwise it is concidered '11'.\n")
        
    elif val == "3":
        print("There are 2 options: hit or stand. If you want to draw a card, type 'hit'. If you want to keep your cards, type 'stand'.Each round, computer will ask you to hit or stand. When you type anything, computer will show you the total value of\nyour cards. In the beggining, your opponet draws 2 card but you are not allowed to see one of them which is\n'hidden card'.When you type stand, your opponet will draw cards and you will be able to see\nall of the cards of your opponet.")
    elif val == "4":
        break
    else:
        print("Type numbers only!")

