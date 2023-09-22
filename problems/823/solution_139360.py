def faltante(lista):
    '''retorna o inteiro faltante numa lista (não necessariamente ordenada) de numeros consecutivos; list -> int'''
    k = 1
    lista_ordenada = list.sort(lista)
    falta = 0
    while k < len(lista):
        if (lista_ordenada[k-1] + lista_ordenada[k])%2 == 0:
            falta = falta + (lista_ordenada[k-1] + lista_ordenada[k])/2
        elif lista_ordenada[0] != 1:
            falta = falta + 1
        k = k + 1    
    return falta