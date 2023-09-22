def melhor_volta(matriz):
    volta=0
    corredor = 0
    n=0
    melhortempo = 9999999
    while n < 6:
       	for tempos in matriz[n]:
        	if tempos < melhortempo:
        		melhortempo = tempos
        		corredor = n+1
        		volta = list.index(matriz[n],tempos)
         
        n=n+1
    resultado=(corredor,melhortempo,volta)
    return resultado