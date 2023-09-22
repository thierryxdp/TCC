def qtd_divisores(n):
    '''Retorna quantos divisores um numero tem;
       Entrada: int;
       Saida: int;
    '''
    i = []
    for x in range(1, n+1):
        if n%x==0:
            list.append(i, x)
    return len(i)