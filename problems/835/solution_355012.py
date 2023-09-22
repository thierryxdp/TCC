def melhor_volta(matriz):
    voltas=[]
    
    for linha in matriz:
        melhor=min(linha)
        list.append(voltas, melhor)
        if min(voltas) in linha:
            a=matriz.index(linha) + 1
    a=(a,min(voltas))