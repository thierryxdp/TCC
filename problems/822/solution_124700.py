def repetidos(num):
    '''Recebe uma lista de números e retorna a quantidade de vezes que um número é igual ao seu anterior.
    list -> int'''
    repeticoes = 0
    i = 0
    c = 1
    a = 0
    b = 0
    while i < len(num):
        a = num[i]
        b = num[c]
        if a == b:
            repeticoes = repeticoes + 1
        i = i + 1
        c = c + 1
    return repeticoes