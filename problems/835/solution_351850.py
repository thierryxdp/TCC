def melhor_volta(matriz):
    volta=0
    corredor = 0
    n=0
    tempo = 9999999
    while n < 10:
       	for x in matriz[n]:
        	if x < tempo:
        		tempo = x
        		corredor = n+1
        		volta=(list.index(matriz[n], x )+1)
         
        	n=n+1
    resultado=(corredor,tempo,volta)
    return resultado