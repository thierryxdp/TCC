def qtd_divisores (numero):
    '''Retorna a quantidade de divisores de um dado número n.
    int -> int'''
    divisores = []
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append (divisores, i)
    return len(divisores)