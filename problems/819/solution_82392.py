def filtraMultiplos(lista,n):
    """Essa função retorna os números da lista que são múltiplos de n
    Parametro de entrada = list, int
    Parametro de saída = list"""
    proximo=0
    Multi=[]
    while proximo<len(lista):
        m=lista[proximo]%n
        if m==0:
            list.append(Multi,lista[proximo])
        proximo=proximo+1
    return Multi