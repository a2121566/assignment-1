class mobile:
    def __init__(self,color="",price=0,year_of_manufacture=0):
        self._color=color
        self._price=price
        self._year_of_manufacture=year_of_manufacture
    def getcolor(self):
        return self._color
    def getprice(self):
        return self._price
    def getyear_of_manufacture(self):
        return self._year_of_manufacture
    def setprice(self,price):
        self._price=price
    def __str__(self):
        return "The mobile color: "+self._color+"\n"+"The year of manufacture: \
"+str(self._year_of_manufacture)+"\n"+"The price: "+str(self._price)


class sony(mobile):
    def __init__(self,color="",price=0,year_of_manufacture=0,System_version=0.0):
        super().__init__(color,price,year_of_manufacture)
        self._System_version=System_version
    def info(self):
        return "The mobile is manufactured by sony\nThe System Edition is: \
"+str(self._System_version)+"\n"+"The price is: "+str(self._price)+"$"+"\n"+"The color is: "+str(self._color)

class samsung(mobile):
    def info(self):
        return "The mobile is manufactured by SAMSUNG"+"\n"+"The price is: "+str(self._price)+"$\
"+"\n"+"The color is: "+str(self._color)
        
    
