def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores que um inteiro
    possui. int -> int'''
    lista = []
    for x in range(1, n+1):
        if n % x == 0:
            lista = lista + [x,]
    return len(lista)