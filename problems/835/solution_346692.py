def melhor_volta(matriz):
    lista=[]
    indice=0
    for l in matriz:
        menorvolta=min(matriz[indice])
        list.append(lista, menorvolta)
        indice=indice +1
    melhorcompetidor=list.index(lista,min(lista))+1
    melhorvolta=matriz[melhorcompetidor-1]
    resultado=melhorcompetidor,min(lista),melhorvolta
    return resultado