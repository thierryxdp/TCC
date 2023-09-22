def qtd_divisores(num):
    """ ddo um numero retorna a quantidade de divisores que esse numero tem.
    entra inteiro -> inteiro. """
    
    d = list(range(1, num))
    divisores = 0
    
    if num <= 0:
       	return divisores
    
    for proximo in d:
        print (proximo)
        if num%proximo == 0:
            divisores = divisores + 1
    return divisores