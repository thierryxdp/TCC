def soma_h(termo):
    """
    	recebe um n para calcular um somatória até esse n termo.
        int --> int
    """
    soma = 0
    n = 1
    while n <= termo:
        soma += (1/n)
        n += 1
    
    return round(soma, 2)