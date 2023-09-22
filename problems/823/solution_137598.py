def faltante(l):
    '''
    	A função recebe uma listá contendo números inteiros de 1 a n menos um número
        desse intervalo. Com isso, o código retorna qual o número que está faltando.
        l -> lista contendo n-1 elementos, sendo esses elementos números inteiros
        pertecentes ao intervalo de 1 a n.
        list -> int
    '''
    l.sort()
    i = 0
    x = 0
    c = 0
    while i <len(l):
        if i+2== l[c]:
            x = i+1
            c += 1
        c += 1
        i += 1
    return x