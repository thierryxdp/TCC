import numpy as np
def melhor_volta(numeros):
    melhor=[]
    for k in numeros:
        minimo = min(k)
        min_index=[]
        for i in range(0,len(k)):
            if minimo == k[i]:
                min_index.append(i)
            	melhor.append([round(minimo,2),min_index[0]])
    idx = np.where(numeros.round(2)==numeros.round(2).min())[0]
    piloto = idx[0] 
    tempo, volta = min(melhor)[0], min(melhor)[1]
    return (piloto, tempo,volta)