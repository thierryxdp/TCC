def maiores(l, n):
    '''
    Esta função recebe uma lista contendo, números inteiros, e um número inteiro.
    Retorna uma lista contendo todos os números da listaoriginal que sejam maiores que o número fornecido.
    
    Parametros
    ----------
    l (list) : lista
    n (int) : número inteiro
    '''
    l.append(n)
    l.sort()
    return l[l.index(n)+1:]