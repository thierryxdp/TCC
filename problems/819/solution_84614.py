def filtramultiplos(lista, numero):
    '''filtra os multiplos de uma lista e retorna uma outra lista com esses mesmo numeros
    :param lista: list->list
    :param numero: int->int
    :return: list->list
    '''
    i=0
    nova lista=[]
    while i<len(lista):
        if lista[i]%numero==0:
            nova lista.append(lista[i])
        i+=1
       return novalista