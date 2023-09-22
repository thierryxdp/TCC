def melhor_volta(matriz):
    nvoltas = len(matriz)
    ntempos = len(matriz[0])
    i = 0
    list = []
    
    while i < nvoltas:
        a = min(matriz[i])
        list = list + [a]
        i = i + 1
        
    menor = min(list)  
    #qual_volta = 
    #seguir = matriz[qual_volta]
    #quem_foi = seguir.index(menor)
    return list
    #return (quem_foi,menor, qual_volta)