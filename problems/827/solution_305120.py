def qtd_divisores(n):
    '''Adiciona todos os divisores de n em uma lista e retorna o tamanho da lista
    int -> int'''
    lista = []
    for x in range(1,n+1):
        if n % x  == 0:
            lista.append(x)
    return len(lista)