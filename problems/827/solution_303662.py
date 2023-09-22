def qtd_divisores(numero):
    """Função que conta a quantidade de divisores que um número tem.
    Entrada: int.
    Saída: int."""
    
    divisores = []
    
    for num in range(1,numero+1):
        if numero%num == 0:
            list.append(divisores, num)
    qnt_divisores = len(divisores)
    
    return qnt_divisores