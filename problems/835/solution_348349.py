def melhor_volta(matriz):
    lista=[]
    i=0
    for corredor in matriz:
        menorTempo=min(corredor)
        lista.append(i+1)
        lista.append(menorTempo)
        i+=1
    return lista