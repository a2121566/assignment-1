the_names = ['ALAA','HAYA','AHMAD','ALI','KARAM']
name= input("Enter the name of the student:")
name=name.upper()
if (name in the_names):
    print (name+" is graduate.")
else:
    print (name+" is non-graduate.")

