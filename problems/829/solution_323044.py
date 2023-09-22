def soma(n):
    """ A funçao soma, calcula o valor H com N termos onde N é inteiro e dado com entrada
        
        Parameters:
            n = numero inteiro
            
        Testes:
            soma(2) = 1
            soma(3) = 1.5
            soma(10) = 2.83
            
        Returns:
            valor H com N termos onde N é inteiro e dado com entrada.
            int --> float
    """
    resultado = 0
    for i in range(2,n+1):
        resultado = resultado + (1/i)
    return round(resultado,2)

    
print (soma(2), soma(3), soma(10))