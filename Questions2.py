while 1:
    print ("enter -1 to exit")
    D_num = int(input("enter decimal numbe: "))

    if D_num==-1:
        break

    B_num = []
    
    while D_num!=0:
        y= D_num %2
        B_num.append(y)
        D_num=D_num//2
        
    B_num.reverse()
    B_num_s=[]
    for i in B_num:
        B_num_s.append(str(i))
        
        
    print ("the binary number is: "+"".join(B_num_s))
    
    
