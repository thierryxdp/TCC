def faltante(lista):
    f=1
    proximo=0
    while f<=len(lista)+1:
        if f!= lista[proximo] and f<= len(lista):
            return f 
        proximo= proximo+1
        f=f+1