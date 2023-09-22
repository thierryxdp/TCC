def repetidos(l):
    '''função que recebe como entrada uma lista de números (l)
    e retorna o número de vezes que algum elemento da lista é
    igual ao anterior'''
    n=0
    anterior=0
    while n <len(l):
        if n == n in l:
            n = n + (l[anterior],)
        anterior = anterior - 1
    return n