def qtd_divisores(n):
    """
    Encontra o número de divisores de um número
    int -> list
    """
    
    l = []

    for i in range(1, n):
        x = i % n
        if x == 0:
            l.append(i)
        
    return len(l)

    #qtd_divisores(10) -> 1,2,5,10