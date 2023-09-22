def filtraMultiplos(lista,numero):
    """Função que filtra os multiplos de um numero dentro da lista; list,int->list """
    nova=[]
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%numero == 0:
            list.append(nova,lista[proximo])
        proximo= proximo+1
    return nova