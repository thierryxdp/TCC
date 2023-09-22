def repetidos(lista):
    '''recebe lista e retorna quantas vezes um elemento
    é igual ao elemento anterior.
    entrada: list
    saida: list'''
    rep=[]
    proximo=0
    while proximo < len(lista):
        if lista[proximo] == lista[proximo-1]:
            list.append(rep,lista[proximo]) 
        proximo = proximo + 1
    return len(rep)