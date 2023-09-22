def conta_numero(numero,matriz):
    '''Retorna o numero de vezes que um determinado número inteiro aparece em uma matriz qualquer com números inteiros.int->int.'''
    lista=[]
    for n in range(len (matriz)):
        if numero in matriz[n]:
            c=list.count(matriz[n],numero)
            list.append(lista,c)
    return int(sum(lista))