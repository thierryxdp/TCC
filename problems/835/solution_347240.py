def melhor_volta(matriz):
    corredor = 0
    menor = matriz[0][0]
    
    for i in matriz:
        a = min(i)
        if a < menor:
            menor = a
    for i in matriz:
        corredor +=1
        if menor in i:
            volta = i.index(menor)
            return((corredor,menor, volta+1))