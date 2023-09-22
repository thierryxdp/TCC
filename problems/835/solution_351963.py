def melhor_volta(matriz):
    lista=[]
    vencedor=()
    for i in range(len(matriz)):
        list.append(lista,min(matriz[i]))
        tempo=min(lista)
        compet=list.index(lista,tempo)
        final=list.index(matriz[compet],tempo)
        vencedor=(compet+1,tempo,final+1)
    return vencedor