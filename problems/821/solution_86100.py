def fatorial (numero):
    """Função que, dado um número, calcular o fatorial.
    Entrada: int.
    Saída: int."""
    
    res_fatorial = 1
    conta = 1
    
    while conta <= numero:
        res_fatorial = res_fatorial * conta
        conta = conta + 1
    return res_fatorial