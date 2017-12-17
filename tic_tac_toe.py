# This program allows the user to play Tic-Tac-Toe against a partner or against the computer.

import turtle

def drawgrid(ss):# Draws the tic-tac-toe grid; ss = side length of one square
    turtle.seth(0)
    turtle.pu()
    turtle.goto(-1.5*ss, -0.5*ss)
    turtle.pd()
    turtle.fd(3*ss)
    turtle.pu()
    turtle.goto(-1.5*ss, 0.5*ss)
    turtle.pd()
    turtle.fd(3*ss)
    turtle.pu()
    turtle.goto(-0.5*ss, 1.5*ss)
    turtle.pd()
    turtle.right(90)
    turtle.fd(3*ss)
    turtle.pu()
    turtle.goto(0.5*ss, 1.5*ss)
    turtle.pd()
    turtle.fd(3*ss)
    

def drawX(xx, yy, s): # s and sss are the leg of the X and the radius of O respectively 
    turtle.pu()
    turtle.goto(xx, yy)
    turtle.seth(0) # Unnecessary but easier to understand
    turtle.lt(135)
    turtle.pd()
    turtle.fd(s)
    turtle.bk(2*s)
    turtle.fd(s)
    turtle.left(90)
    turtle.fd(s)
    turtle.bk(2*s)

def drawO(xxx, yyy, sss):
    turtle.pu()
    turtle.goto(xxx, yyy-sss)
    turtle.seth(0)
    turtle.pd()
    turtle.circle(sss)

def magic(numm): # Takes a square number and gives it the 'magic square' equivalent.
    if numm == 1:
        numm = 2
    elif numm == 2:
        numm = 9
    elif numm == 3:
        numm = 4
    elif numm == 4:
        numm = 7
    elif numm == 5:
        numm = 5
    elif numm == 6:
        numm = 3
    elif numm == 7:
        numm = 6
    elif numm == 8:
        numm = 1
    elif numm == 9:
        numm = 8

    return numm

def pos(sqr, distt):
    if sqr == 2:
        return distt, distt
    if sqr == 9:
        return 0, distt
    if sqr == 4:
        return -distt, distt
    if sqr == 7:
        return distt, 0
    if sqr == 5:
        return 0, 0
    if sqr == 3:
        return -distt, 0
    if sqr == 6:
        return distt, -distt
    if sqr == 1:
        return 0, -distt
    if sqr == 8:
        return -distt, -distt
        
def winner(p1, p2): # Checks to see if there are any two tokens in a the two sets that have the potential to make a three-in-a row, or it will check to see if anyone was already won.
    nummm = 0
    for o in p1:
        sub = 15 - o
        i = p1.index(o)
        p1.remove(o)
        for oo in p1:
            subb = sub - oo
            if subb in p1 and subb != oo:
                p1.append(o)
                return "p wins"
            if subb not in p1 and subb not in p2 and 0 < subb < 10:
                nummm = subb
        p1.insert(i, o)
    if nummm != 0 and nummm not in p1 and nummm not in p2:
        #print nummm
        return nummm
    mergedl = p1 + p2
    if 1 in mergedl and 2 in mergedl and 3 in mergedl and 4 in mergedl and 5 in mergedl and 6 in mergedl and 7 in mergedl and 8 in mergedl and 9 in mergedl:
        return "draw"
    return "nothing"

def userm(comppp, userrr):
    loop = 0
    while loop == 0:
        m = int(raw_input("It's your move. Type 1 to put an X in the top right corner, a 2 for the top corner, 3 for the top left hand corner, 4 for center-right, 5 for center, 6 for center-left, 7 for bottom-right, 8 for bottom, and 9 for bottom-left."))
        if magic(m) not in comppp and magic(m) not in userrr:
            return magic(m)
            loop =+ 1
        print "You can't move there."

def compm(compp, userr):
    if winner(compp, userr) != "nothing" and winner(compp, userr) != "draw":
        #print "1"
        return winner(compp, userr)
    if winner(userr, compp) != "nothing" and winner(userr, compp) != "draw":
        print "2"
        print winner(userr, compp)
        print winner(userr, compp)
        return winner(userr, compp)
        
    if compp == [] and userr == []:
        return magic(5) # This will just be 5.
    if compp == [] and len(userr) == 1:
        #print "3"
        if userr[0] == 5:
            return magic(9)
        if userr[0] != 5:
            return magic(5) # Gets to one move both sides.
    if compp == [5]:
        #print "4"
        if userr == [magic(2)]:
            return magic(9)
        if userr == [magic(4)]:
            return magic(3)
        if userr == [magic(6)]:
            return magic(1)
        if userr == [magic(8)]:
            return magic(2) # These cases will run on their own as a result of the winner function.

        if userr == [magic(1)]:
            return magic(9)
        if userr == [magic(3)]:
            return magic(7)
        if userr == [magic(7)]:
            return magic(3)
        if userr == [magic(9)]:
            return magic(1)

    if compp == [5] and magic(1) in userr and magic(9) in userr and len(userr) == 2: # One odd scenerio. 
        return magic(2)
    if compp == [5] and magic(3) in userr and magic(7) in userr and len(userr) == 2:
        return magic(8) # Switching it up just for the hell of it... it could be magic(2).
    

    if len(compp) == len(userr):
        if magic(1) not in compp and magic(1) not in userr and magic(2) not in userr and magic(4) not in userr: # Selecting a corner further from action.
            return magic(1)
        if magic(3) not in compp and magic(3) not in userr and magic(6) not in userr and magic(2) not in userr:
            return magic(3)
        if magic(7) not in compp and magic(7) not in userr and magic(4) not in userr and magic(8) not in userr:
            return magic(7)
        if magic(9) not in compp and magic(9) not in userr and magic(8) not in userr and magic(6) not in userr:
            return magic(9)

    if len(userr) > len(compp):
        if magic(1) not in compp and magic(1) not in userr and magic(2) in userr: # Selecting a corner closer to action
            return magic(1)
        if magic(3) not in compp and magic(3) not in userr and magic(6) in userr:
            return magic(3)
        if magic(7) not in compp and magic(7) not in userr and magic(4) in userr:
            return magic(7)
        if magic(9) not in compp and magic(9) not in userr and magic(8) in userr:
            return magic(9)
        
    if magic(1) not in compp and magic(1) not in userr: # Arbitrarly selecting a corner. 
        return magic(1)
    if magic(3) not in compp and magic(3) not in userr:
        return magic(3)
    if magic(7) not in compp and magic(7) not in userr:
        return magic(7)
    if magic(9) not in compp and magic(9) not in userr:
        return magic(9)
    
    if magic(2) not in compp and magic(2) not in userr:# If all corners are taken, the function will arbitrarly chose a side.
        return magic(2)
    if magic(4) not in compp and magic(4) not in userr:
        return magic(4)
    if magic(6) not in compp and magic(6) not in userr:
        return magic(6)
    if magic(8) not in compp and magic(8) not in userr:
        return magic(8)

    
            
# End of functions


print "This is a tic-tac-toe game you cannot win. Do you not believe me? Let's play, I'll be O. ;)"
play = raw_input("Do you want to play?")

while play == "yes" or play == "Yes" or play == "oui" or play == "Oui" or play == "YES" or play == "HELL YES" or play == "HELL YA" or play == "hell ya" or play == "yes " or play == " yes":
    turtle.clear()
    drawgrid(150)
    start = int(raw_input("If you want to start, type 1, if you'd prefer me to start, type 0."))

    comp = []
    user = []

    size = 70
    dist = 150
    status = "playing"
    while status == "playing":
        if start == 0:
            drawO(0, 0, size)
            comp.append(5)
            start += 2

        um = userm(comp, user)
        drawX(pos(um, dist)[0], pos(um, dist)[1], size)
        user.append(um)

        if winner(user, comp) == "p wins":
            status = "user wins"
        if winner(user, comp) == "draw":
            status = "draw"
        
        if status == "playing":
            cm = compm(comp, user)
            print comp, user, cm
            drawO(pos(cm, dist)[0], pos(cm, dist)[1], size)
            comp.append(cm)
            
            if winner(comp, user) == "p wins":
                status = "comp wins"
            if winner(comp, user) == "draw":
                status = "draw"

    if status == "draw":
        print "DRAW. Good game, you played well."
    if status == "user wins":
        print "YOU WIN. Wow! This is an impossiblity, kudos."
    if status == "comp wins":
        print "I WIN. Better luck next time."

    play = raw_input("Do you want to play again?")

print "Thank you for playing!"

        
        

