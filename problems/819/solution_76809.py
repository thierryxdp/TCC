def filtraMultiplos(lista,num):
    """ """
    resposta=[]
    indice=0
    while indice <len(lista):
        if lista[indice]%num==0:
            resposta.append(lista[indice])
        indice +=1
    return resposta