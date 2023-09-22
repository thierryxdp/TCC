def conta_numero(n, m):
    '''Dado um número inteiro(n) e uma matriz(m) qualquer,
    conta e retorna quantas vezes n aparece em m.
    int,list->int'''
    i = 0
    contador = 0
    for lista in m:
        contador = contador + list.count(m[i], n)
        i = i + 1
    return contador