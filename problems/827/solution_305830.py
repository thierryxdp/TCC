def qtd_divisores(n):
    '''retorna quantos divisores o numero inteiro fornecido tem.
    int -> int'''
    i =1
    lista_de_divisores = []
    while i <= n:
        if n % i == 0:
            lista_de_divisores.append(i)
        i += 1
    return len(lista_de_divisores)