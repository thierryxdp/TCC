def soma_h(n):
    """ A funçao soma_h, calcula o valor H com N termos onde N é inteiro e dado com entrada.
        
        Parameters:
            n = numero inteiro
        Testes:
            soma_h(2) = 1
            soma_h(3) = 1.5
            soma_h(10) = 2.83
            
        Returns:
            valor H com N termos onde N é inteiro e dado com entrada.
            int --> bool
    """
    resultado = 1
    for i in range(2,n):
        resultado = resultado + (1/i)
    return round(resultado,2)