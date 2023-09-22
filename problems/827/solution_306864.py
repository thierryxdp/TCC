def qtd_divisores(n):
    '''Retorna o número de divisores de um número n.
    int --> int'''
    
    divisores_de_n = []

    for i in range(n):
        if n%i == 0:
            divisores_de_n.append(i)
           
    num_div = len(divisores_de_n)

    return num_div