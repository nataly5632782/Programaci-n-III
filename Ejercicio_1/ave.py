from animal import animal 
from datetime import datetime
class ave (animal):
     def __init__(self,nacimiento, propietario,nombre, peso):
         
         self.naci1= nacimiento 
         self.prop= propietario 
         super().__init__(nombre, peso)
     
     
     def printdatos(self):
       fecha2=datetime.now()
       fecha3=(fecha2.year)
       edad= fecha3-self.naci1
       if(edad>5):
           print("Es mayor de edad")
       else:
           print("Es menor de edad")
       

         
         
         
x= ave(2005,"luca","PALOMA",12)
x.printdatos()
