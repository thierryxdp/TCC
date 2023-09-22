def faltante(L):
    """Função que irá descobrir qual número inteiro deste intervalo que está faltando; list->init"""
    lista= list(range(1,len(L)+5))
    index= 0
    list.extend (L, [0,0,0])
    while lista[index]==L[index]:
        index=index+1
    return lista[index]