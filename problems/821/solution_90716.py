numero= int(input('digite um numero:'))
fatorial=numero
contador=1
while(numero-contador)>1:
    fatorial=fatorial*(numero-contador)
    contador+=1
print('{0}! = {1}'. format(numero,fatorial))