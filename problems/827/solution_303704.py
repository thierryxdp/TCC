def qtd_divisores(n):
    """ A funçao qtd_divisores conta quantos divisores o número inserido tem. 
        
        Parameters:
            n = numero a ser analisado seus divisores

        Testes:
            qtd_divisores(4) = 33
            qtd_divisores(2) = 3
            qtd_divisores(3) = 9
            
        Returns:
            soma dos fatoriais dos números inteiros de 1 a n.
            int --> int
    """
    resultado = 0
    for i in range(1,n+1):
        if n%i == 0:
            resultado = resultado + 1

    return resultado