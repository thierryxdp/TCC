def filtraMultiplos(lista,numero):
    #checar se o resultado da multiplicaçao entre 2 numeros inteiros
    #esta na lista
    #se estiver adicionar a uma lista
    contador=0
    elementoProximo=0
    listaMultiplos=[]
    while contador<len(lista):
        calculo=lista[elementoProximo]%numero
        contador+=1
        if calculo==0:
            list.append(listaMultiplos,lista[elementoProximo])
            elementoProximo+=1
        else:
            elementoProximo+=1
    return listaMultiplos