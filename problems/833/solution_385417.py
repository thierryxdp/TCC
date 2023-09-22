def conta_numero(n,mt):
    '''Dado uma matriz de número de inteiros e um número inteiro,
retorna quantas vezes vezes o número inteiro dado aparece na matriz.
    int, list -> int'''
    qnt = 0
    j = 0
    i = 0
    while i < len(mt):
        c = list.count(mt[j], n)
        qnt = qnt + c 
        j = j+ 1
        i = i + 1