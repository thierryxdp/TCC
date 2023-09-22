def qtd_divisores(numero):
    '''Retorna o número de divisores do número recebido.
    int -> int'''
    lista = list(range(1,numero+1))
    divisores = []

    for n in lista:
        if numero//n == numero/n:
            list.append(divisores,n)
    
    return len(divisores)