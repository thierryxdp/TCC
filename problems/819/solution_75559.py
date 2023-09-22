def filtraMultiplos(lista,numero):
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%numero == 0:
            multiplos= multiplos + lista[proximo]
        proximo=proximo+1
    return multiplos