def melhor_volta(matriz):
    lista=[]
    for i in matriz:
        for k in i:
            lista.append(k)
            melhor=min(lista)
            
    return (i,melhor)