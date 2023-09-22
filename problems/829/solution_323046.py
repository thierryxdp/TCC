def soma():
    """ A funçao soma, calcula a conta estipulada na foto do machine teaching.
        
        Parameters:
            
        Testes:
            soma() = 6.59
            
        Returns:
            resultado da conta estipulada na foto do machine teaching.
             --> float
    """
    cont = -1
    resultado = 0
    for i in range(1,11):
        cont = cont * -1
        fatorial = 1
        for x in range(1,i+1):
            fatorial = fatorial * x
        resultado = resultado + ((11 - i)/fatorial*cont)
    return round(resultado,2)