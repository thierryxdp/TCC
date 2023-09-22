def qtd_divisores(numero):
    ''' retorna a quantidade de divisores um número inteiro tem.
    int -> int'''

    divisores = []
    
    for i in range(1,numero+1):
        if (numero%i) == 0:
            list.append(divisores, i)
    return len(divisores)