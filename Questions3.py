import json

while "true":
    x=int(input("press 1 to: translator developer or 2 to translator user"))
    if x==1:
        file_r=open('D.json', 'r')
        j_p = json.load(file_r)
        while "true":

            word=input("Write english word: ")
            word=word.upper()

            translate=input("Write the Arabic translation: ")
            translate=translate.upper()

            j_p[word]=translate

            z=input('enter EXIT to exit translator developer.')
            z=z.upper()
            
            if z=='EXIT':
                j_p = json.dumps(j_p)
                with open("D.json", "w") as file_w:
                    file_w.write(j_p)
                break

    else:
        while "true":
            file_r=open('D.json', 'r') 
            j_p = json.load(file_r)
            word=input("enter the english word: ")
            word=word.upper()
            if word == "EXIT":
                break
            if word in j_p:
                print("Translat: "+j_p[word])
            else:
                print ("word not found")
            print ("enter EXIT to exit translator user")
            
