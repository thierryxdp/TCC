def filtraMultiplos(lista,numero):
    #checar se o resultado da multiplicaçao entre 2 numeros inteiros
    #esta na lista
    #se estiver adicionar a uma lista
    contador=0
    elementoProximo=0
    num=1
    listaMultiplos=[]
    while contador+4<len(lista):
        calculo=numero*num
        num+=1
        contador+=1 
        if calculo in lista:
            list.append(listaMultiplos,calculo)
        else:
            pass
	return listaMultiplos