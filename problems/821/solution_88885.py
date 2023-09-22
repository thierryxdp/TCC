def fatorial(numero):
    '''funcao fornece o fatorial de um numero,entrada/saida:int'''
    lista_numero= list(range(numero+1))
    list.remove(lista_numero,0)
    fat=1
    indi=0
    while indi<len(lista_numero):
        fat=fat*lista_numero[indi]
        indi=indi+1
    return fat