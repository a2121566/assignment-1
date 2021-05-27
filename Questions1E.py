L=["Network" , "Math" , "Programming", "Physics" , "Music"]
y=0
s=[]
for i in L:
    x =len(i)
    if x>y:
        y=x
        s=i
print ("the longest item in list is "+s+" And its length "+str(y))

