def qtd_divisores(n):
    '''
    Retorna a quantidade de divisores
    do numero n.
    int -> int
    '''
    divisores = []
    for valores in range(1, n + 1):
        if n%valores == 0:
            list.append(divisores,valores)
            
    return len(divisores)