def qtd_duvisores(numero):
    """ função que recebe um número como entrada e retorna
    	sua quantidades de divisores. int --> int """
    
    quantDivisores = 0
    divisor = 1
    while divisor <= numero:
        if numero%divisor == 0:
            quantDivsiores +1
    return quantDivisores