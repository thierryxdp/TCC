def faltante(L):
    '''funcao que recebe como entrada uma lista L de tamanho N-1 com inteiros numerados de 1 a N e retorna o numero inteiro que pertence ao intervalo [1,n] mas nao pertence a lista L
    list -> int'''
    i=1
    numero_faltante=0
    lista_completa=list.sort(L)
    while i<len(L):
        if L[i]-L[i-1]!=1:
            numero_faltante=numero_faltante+L[i-1]+1
            lista_completa=list.insert(lista_completa,lista_completa[i],lista_completa[i-1]+1)
        i=i+1
    return lista_completa