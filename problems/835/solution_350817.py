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
    qual_indice = list.index(menor)
    volta = qual_indice + 1
    seguir = matriz[qual_indice]
    #quem_foi = seguir.index(menor)
    return seguir
    #return (quem_foi,menor, qual_volta)