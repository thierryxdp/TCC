def total(lista,preco):
    '''explicação'''

    valor_total = 0

    for i in range(0,len(lista)):
        valor_total = valor_total + dict.get(preco,lista[i],0)

    return valor_total