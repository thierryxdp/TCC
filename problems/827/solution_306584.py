def qtd_divisores(n):
    '''Função que recebe um número n e retorna o número de
    divisores de n
    int -> int'''
    lista_de_divisores = []
    for valor in range(1, n+1):
        if n%valor == 0:
            lista_de_divisores = lista_de_divisores + [valor]
    numero_divisores = len(lista_de_divisores)
    return numero_divisores