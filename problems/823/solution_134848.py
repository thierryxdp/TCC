def faltante(L):
    '''funcao que recebe como entrada uma lista L de tamanho N-1 com inteiros numerados de 1 a N e retorna o numero inteiro que pertence ao intervalo [1,n] mas nao pertence a lista L
    list -> int'''
    i=0
    list.sort(L)
    num_faltante=0
    if 1 not in L:
        return 1
    while i+1<len(L):
        if L_[i]+1!=L[i+1]:
            num_faltante=num_faltante+L[i]+1
        i=i+1
    else:
        return L[-1]+1