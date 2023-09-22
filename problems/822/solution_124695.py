def repetidos(num):
    '''Recebe uma lista de números e retorna a quantidade de vezes que um número é igual ao seu anterior.
    list -> int'''
    repeticoes = 0
    i = 0
    while i < len(num):
        if num[i] == num[i+1]:
            repeticoes = repeticoes + 1
    return repeticoes