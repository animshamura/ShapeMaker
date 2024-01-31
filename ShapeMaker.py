def FilledTriangle():
    print()
    for i in range(1,10):
        for j in range(1,i+1): print("*",end=" ")
        print()
    print()

def HollowTriangle():
    print()
    for i in range(1,10):
        for j in range(1,i+1):
            if(j==1 or j==9 or j==i or i==9): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

def FilledPyramid():
    print()
    for i in range(1,10):
        print(" "*(9-i), end=" ")
        for j in range(1,i+1): print("*",end=" ")
        print()
    print()

def FilledRectangle():
    print()
    for i in range(1,10): 
        for j in range(1,10): print("*",end=" ")
        print()
    print()

def HollowRectangle():
    print()
    for i in range(1,10): 
        for j in range(1,8): 
            if(j==1 or j==7 or i==1 or i==9): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

def OneDiagonalRectangle():
    print()
    for i in range(1,10): 
        for j in range(1,8):
            if(j==1 or j==7 or j==i or i==1 or i==9 or i==7): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

def TwoDiagonalRectangle():
    print()
    for i in range(1,10): 
        for j in range(1,8): 
            if(j==1 or j==7 or j==i or j==8-i or i==1 or i==9 or i==7): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

def OneDiagonalSquare():
    print()
    for i in range(1,8): 
        for j in range(1,8): 
            if(j==1 or j==7 or j==i or i==1 or i==7): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

def FilledSquare():
    print()
    for i in range(1,10): 
        for j in range(1,10): print("*",end=" ")
        print()
    print()

def HollowSquare():
    print()
    for i in range(1,8): 
        for j in range(1,8): 
            if(j==1 or j==7 or i==1 or i==7): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

def TwoDiagonalSquare():
    print()
    for i in range(1,8): 
        for j in range(1,8): 
            if(j==1 or j==7 or j==i or j==8-i or i==1 or i==7): print("*",end=" ")
            else: print(" ",end=" ")
        print()
    print()

while(True):
    print("Wanna get a shape? Enter 1, otherwise 2") 
    q1 = int(input())
    if(q1==2): break
    print("1 for Filled Triangle")
    print("2 for Hollow Triangle")
    print("3 for Filled Pyramid")
    print("4 for Filled Rectangle")
    print("5 for Hollow Rectangle")
    print("6 for One Diagonal Rectangle")
    print("7 for Two Diagonal Rectangle")
    print("8 for Filled Square")
    print("9 for Hollow Square")
    print("10 for One Diagonal Square")
    print("11 for Two Diagonal Square")
    q2 = int(input())
    if(q2==1): FilledTriangle()
    elif(q2==2): HollowTriangle()
    elif(q2==3): FilledPyramid()
    elif(q2==4): FilledRectangle()
    elif(q2==5): HollowRectangle()
    elif(q2==6): OneDiagonalRectangle()
    elif(q2==7): TwoDiagonalRectangle()
    elif(q2==8): FilledSquare()
    elif(q2==9): HollowSquare()
    elif(q2==10): OneDiagonalSquare()
    elif(q2==11): TwoDiagonalSquare()
    else: print("Wrong Input!")

