def fatorial(numero):
    """ A funçao fatorial, dado um número, calcula o fatorial deste número.
        
        Parameters:
            numero = numero a ser calculado o fatorial

        Testes:
            fatorial(10) = 3628800
            fatorial(5) = 120
            fatorial(3) = 6
            
        Returns:
            fatorial do numero inserido
            int --> int
    """
    i = 2
    resultado = 1
    while numero>=i:
        resultado = resultado * i
        i = i+1
    return resultado