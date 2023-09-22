def faltante(lista):
    f=1
    proximo=0
    while f<len(lista):
        if f!= lista[proximo]:
            return f
        proximo= proximo+1
        f=f+1