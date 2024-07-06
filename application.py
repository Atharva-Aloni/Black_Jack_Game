import random as rm    
l = [1,2,3,4,5,6,7,8,9,10,10,10,10]
bol=[True,False]
def stats(player,i):
      print(f"Player name : {player[i]['name']}")
      print(f"Player amount : {player[i]['amount']}")
      
def dealer_play(v):
  
    while(True):
        s=0
        for i in v['cards']:
            s+=i
        print(f"Dealer cards : {v['cards']}")    
        print(f"Dealer cards total : {s} ")
        if(s>21):
            print("Dealer is Busted ")
            v['eligible']=True
            break;
        else:
            if(s<=17):
                y=rm.choice(l)
                if(y==1):
                    if(rm.choice(bol)):
                        y=11
                    else:
                        y=1
                v['cards'].append(y)
            else:
                b = rm.choice(bol)
                if(b):
                    v['sum']=s
                    v['eligible']=False
                    break
def player_play(v,i):
    
    while(True):
        s=0
        for j in v[i]['cards']:
            s+=j
        if(s>21):
            print(f"Player cards ({v[i]['name']}) : {v[i]['cards']}") 
            print(f"Player {v[i]['name']} is Bust due to card value more than 21 ")
            print()
            v[i]['eligible']=False
            print()
            break;
        
        print(f"Current total of the cards {v[i]['name']} = ${s}") 
        ch = input("Enter H for HIT , or S for STAND : ")
        if(ch=='h' or ch=='H'):
            y=rm.choice(l)
            if(y==1):
                y = int(input("What you want to consider Ace , 1 or 11 = "))
            v[i]['cards'].append(y)
        else:
            v[i]['sum']=s
            print()
            break;
        
def two_cards(v1,v2):
    y = rm.choice(l)
    v2['cards']=[y]
    for i in range(0,len(v1)):
        y=rm.choice(l)
        z=rm.choice(l)
        t=[]
        t.append(y)
        t.append(z)
        v1[i]['cards']=t

    print()
    print("Current card of all player as follow : ")
    print(f"Dealer cards : {v2['cards']} ") 
    for i in range(0,len(v1)):
        print(f"player name : {v1[i]['name']}")
        print(f"player cars : {v1[i]['cards']}")
def print_player(v):
    for i in range(0,len(v)):
        print(f"Player name : {v[i]['name']}")
        print(f"Player amount : ${v[i]['amount']}")
def line():
    for i in range(0,60):
        print("-",end="")
    print()    
player =[]
print("........................Welcome to Black Jack game ......................")
n = int(input("Enter the Number of players : "))
am = int(input("Enter the Intial Amount to every player : $ "))       
for i in range(n):
        name=input(f"Enter the Player {i+1} name : ")
        player.append({'name':name,'amount':am,'eligible':True})
line()
print_player(player)
print()
print("This are the current stats of the players ")
line()
co=1
dealer={}
while(True):
    ch = input("Enter 'exit' for quiting game = ")
    if(ch=="exit"):
          break;
    bet = int(input(f"Enter the betting amount for the {co} round : $ "))
    co+=1
    for i in range(0,len(player)):
        if(player[i]['amount']>=bet):
            player[i]['amount']-=bet
        else:
            player[i]['eligible']=False
    for i in range(0,len(player)):
        stats(player,i)
    line()        
    two_cards(player,dealer)
    for i in range(0,n):
        if(player[i]['eligible']):
            player_play(player,i)
        line()
    dealer_play(dealer)
    for i in range(0,n):
        if(dealer['eligible'] and player[i]['eligible']):
            player[i]['amount'] +=(bet*2)
        elif(player[i]['eligible'] and player[i]['sum']>dealer['sum']):
            player[i]['amount'] +=(bet*2)
        elif(player[i]['eligible'] and player[i]['sum']==dealer['sum']):
            player[i]['amount']+=bet
    line()
    for i in range(0,n):
        stats(player,i)
    
    
    
        


