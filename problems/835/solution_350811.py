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
    
    f = 0
    while f < len(list):
        if list[f] == menor:
            indice = f
    
    qual_volta = indice
    seguir = matriz[qual_volta]
    quem_foi = seguir.index(menor)
    
    return (quem_foi,menor, qual_volta)