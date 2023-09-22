def soma_h(x):
    '''funcao que dado um numero faz a somatoria da sequencia
    	e retorn o valor reduzido em duas casas decimais
    	x->int
        return: float
    '''
     acumulador = 0
    for contador in range(1, x + 1):
        H = 1 / contador
        acumulador += H

    return round(acumulador, 2)