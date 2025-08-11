import math
cx=0
cy=0
radio=0
x=0
y=0
cateto1=0
cateto2=0
h=0

cx=int(input("ingresa la cordenada x del centro del circulo"))
cy=int(input("ingresa la cordenada y del centro del circulo"))
x=int(input("ingresa la cordenada x del punto"))
y=int(input("ingresa la cordenada y del punto"))
radio=int(input("ingresa el radio del circulo"))

cateto1=abs(cx-x)
cateto2=abs(cy-y)

h=math.sqrt((cateto1**2)+(cateto2**2))

if(h>radio):
    print("el punto esta afuera del circulo")
elif(h<=radio):
    print("el punto esta adentro del circulo")