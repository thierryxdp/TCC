def qtd_divisores(numero):
    '''Retorna uma lista com os divisores do número recebido.
    int -> list'''
    lista = list(range(1,numero+1))
    divisores = []

    for n in lista:
        if numero//n == numero/n:
            list.append(divisores,n)