def qtd_divisores(numero):
    '''Retorna quantos divisores um numero tem;
       Entrada: int;
       Saida: int;
    '''
    divisores = []
    for x in range(1, numero+1):
        if numero%x==0:
            list.append(divisores, x)
    return len(divisores)