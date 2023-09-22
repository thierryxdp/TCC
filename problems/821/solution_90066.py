def fatorial(numero):
    """ faz o fatorial do numero inserido
        
        Parameters:
            numero = numero o qual sera feito fatorial

        Testes:
            fatorial(10) = 3628800
            fatorial(5) = 120
            fatorial(3) = 6
            
        Returns:
            fatorial do numero inserido
            int --> int
    """
    i = 5
    resultado = 1
    while i <= numero:
        resultado = resultado * i
        i=i+1
    return resultado