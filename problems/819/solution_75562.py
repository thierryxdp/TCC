def filtraMultiplos(lista,numero):
    """Essa função retorna uma lista com os multiplos de um numero infprmado em uma lista informada"""
    """list,int->list"""
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%numero == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo=proximo+1
    return multiplos