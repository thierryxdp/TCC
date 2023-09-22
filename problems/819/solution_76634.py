import random

def dado():

  	dado1 = 0
  	dado2 = 1
 	 listaDado1 = []
     listaDado2 = []
  	aux = 0

  	while dado1 != dado2:

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    listaDado1.append(dado1)
    listaDado2.append(dado2) 
    aux +=1
    
  	mediaDado1 = sum(listaDado1)/len(listaDado1)
 	mediaDado2 = sum(listaDado2)/len(listaDado2)

  	return (aux, mediaDado1, mediaDado2)

print(dado())