def faltante(l):
    '''
    	A função recebe uma lista contendo todos os números menos 1 de um intervalo
        de 1 a n (sendo os números desse intervalo inteiros positvos). Com isso, a 
        função retorna qual número do intervalo está faltando.
        l -> list (contendo números inteiros de 1 a n, todos inteiros positivos)
        list -> int
    '''
    l.sort()
    i = 1
    c = 0
    x = 0
    while c < len(l):
        if i+1 == l[c]:
            x = i
            i += 1
        i += 1
        c += 1
    if x == 0:
        return i
    else:
        return x