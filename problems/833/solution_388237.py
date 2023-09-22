def conta_numero(numero,matriz):
    '''função que retorna o número de vezes que certo número aparece na matriz
       int, list -> int'''
    i=0
    vezes=0
    while i<len(matriz):
        vezes=vezes +list.count(matriz[i],numero)
        i=i+1
    return vezes