def maiores(minha_lista,n):
    '''Retorna uma lista de numeros inteiros contendo numeros maiores que n
    int,int-->int'''
    maior_que = n
    filtrados = [x for x in minha_lista if x > maior_que]
    return sorted(filtrados)