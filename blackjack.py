# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:59:19 2019

@author: Advait Panda,Daanish Baig,Sidharth Dinesh
"""
import random

class Player():
    #used to make a player object containing hands and their bets and scores
    def __init__(self,l):
        self.hand=[l]
        self.bet=[]
        self.scp=[]

def deck():
    #function returns a randomly shuffled list(deck) of cards having rank and suit
    #rr-list of ranks;s-list of suits;d-deck of cards
    r=list(range(2,11))+['A','J','Q','K']
    s=['Hearts','Spades','Diamonds','Cloves']
    d=[(rank,suit) for suit in s for rank in r]
    random.shuffle(d)
    return d

def score(hand):
    #function that takes list of cards and calculates the score of the hand
    #s-score of hand;numa-number of aces;hand-list of cards;card-card from list hand
    s=0
    for card in hand:
        if card[0] in range(2,11):
            s+=card[0]
        elif card[0] in 'JQK':
            s+=10
        else:
            s+=11
    #ace can have a value of unity or 11 hence if score>21 value of ace is changed to unity
    numa=len([card for card in hand if card[0] is 'A'])
    while numa>0:
        if s>21:
            numa-=1
            s-=10
        else:
            break
    if s==21:
        return [s,'Blackjack']
    else:
        return [s,str(s)]

def check_pairs(hand):
    #functon to check wheter a given hand conatins only a pair
    if hand[0]==hand[1]:
        return True
    else:
        return False
    
def not_aces(hand):
    #function to check wheter a given hand contains a pair of aces
    if check_pairs[hand] and hand[0][0]=='A':
        return False
    else:
        return True

def double_down(hand,bet,scp,j):
    #function to execute the act od doubling down
    bet[j]*=2
    hand[j].append(random.choice(DECK))
    scp[j]=score(players[i].hand[j])
    print('Score:',scp[j][0],'Hand:',hand[j])
    
#Setting up the deck,no of players and their hands along with the dealer's
DECK=deck()
n=int(input('Enter no of players '))
players=[Player([random.choice(DECK),random.choice(DECK)]) for _ in range(n)]
dealer_hand=[random.choice(DECK),random.choice(DECK)]

#main game logic for player:displays score and hand and asks if they will hit, stay, double down or split
for i in range(n):
    play=True
    length=len(players[i].hand)
    j=0
    while j<length:
        players[i].scp.append(score(players[i].hand[j]))
        print('Score:',players[i].scp[j][0],'Hand:',players[i].hand[j])
        players[i].bet.append(int(input('Enter your bet ')))
        while play:
            print('Score:',players[i].scp[j][0],'Hand:',players[i].hand[j])
            if players[i].scp[j][0]>=21:
                break
            else:
                ch=input("Hit,Stay,Double Down or Split? H for Hit; S for Stay; D for Double Down; P for Split ")
                if ch=='S':
                    play=False
                elif ch=='D':
                    if len(players[i].hand[j])==2:
                        double_down(players[i].hand,players[i].bet,players[i].scp,j)
                        play=False
                    else:
                        print('Cannot double down')
                        
                elif ch=='P':
                    if len(players[i].hand[j])==2:
                        if check_pairs(players[i].hand[j]) and not_aces(players[i].hand[j]):
                            players[i].hand.insert(j+1,[players[i].hand[j].pop[0],random.choice(DECK)])
                            players[i].scp.insert(j+1,score(players[i].hand[j+1]))
                            print('Score:',players[i].scp[j+1][0],'Hand:',players[i].hand[j+1])
                            players[i].bet.insert(j+1,int(input('Enter your bet ')))
                            players[i].hand[j].append(random.choice(DECK))
                            players[i].scp[j]=score(players[i].hand[j])
                            print('Score:',players[i].scp[j][0],'Hand:',players[i].hand[j])
                            length+=1
                        elif check_pairs(players[i].hand[j]):
                            players[i].hand.insert(j+1,[players[i].hand[j].pop[0],random.choice(DECK)])
                            players[i].scp.insert(j+1,score(players[i].hand[j+1]))
                            print('Score:',players[i].scp[j+1][0],'Hand:',players[i].hand[j+1])
                            if players[i].scp[j+1][1]=='Blackjack':
                                players[i].scp[j+1][1]=str(21)
                            players[i].bet.insert(j+1,int(input('Enter your bet ')))
                            players[i].hand[j].append(random.choice(DECK))
                            players[i].scp[j]=score(players[i].hand[j])
                            print('Score:',players[i].scp[j][0],'Hand:',players[i].hand[j])
                            if players[i].scp[j+1][1]=='Blackjack':
                                players[i].scp[j+1][1]=str(21)
                            length+=1
                            play=False
                            j+=1
                        else:
                            print('Cannot split hand')
                    else:
                        print('Cannot split hand')
                else:
                    players[i].hand[j].append(random.choice(DECK))
                    players[i].scp[j]=score(players[i].hand[j])
        j+=1
  
#main game logic for dealer:dealer will hit if score is below 17
scd=score(dealer_hand)
print('Dealer\'s turn')
print('Score:',scd,'Hand:',dealer_hand)
while scd[0]<17:
    dealer_hand.append(random.choice(DECK))
    scd=score(dealer_hand)
    print('Score:',scd[0],'Hand:',dealer_hand)
        
#final conditions for game conclusion    
for i in range(n):
    winnings=0
    for j in range(0,len(players[i].hand)):
        if players[i].scp[j][1]=='Blackjack':
            winnings+=2.5*players[i].bet[j]
        elif players[i].scp[j][0]>21:
            winnings-=players[i].bet[j]
        elif scd[0]>21:
            winnings+=2*players[i].bet[j]
        elif scd[0]>players[i].scp[j][0]:
            winnings-=players[i].bet[j]
        elif scd[0]<players[i].scp[j][0]:
            winnings+=2*players[i].bet[j]
        elif players[i].scp[j][0]==scd[0]:
            winnings+=players[i].bet[j]
        else:
            winnings-=players[i].bet[j]
    print('Total winnings of player {} are {}'.format(i+1,winnings))
