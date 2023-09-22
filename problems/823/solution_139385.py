def faltante(lista):
    '''retorna o inteiro faltante numa lista (não necessariamente ordenada) de numeros consecutivos; list -> int'''
    k = 1
    list.sort(lista)
    falta = 0
    while k < len(lista):
        if (int(lista[k-1]) + int(lista[k]))%2 == 0:
            falta = falta + (lista[k-1] + lista[k])/2
        elif lista[0] != 1:
            falta = 1
        k = k + 1 
    if falta == 0:
        falta = falta + len(lista) + 1
    return falta