def melhor_volta(matriz):
    menor = 0
    corredor = 0
    
    for i in matriz:
        menor = min(i)
    for i in matriz:
        corredor +=1
        if menor in i:
            volta = i.index(menor)
            return((corredor, menor, volta+1))