def primo(numero):
    '''
    	Função que recebe um número 
        inteiro positivo, e retorna
        True se ele é primo ou False,
        caso contrário
        : param numero: int
        : return: bool
    '''
    possiveis_divisores = list(range(2,numero))
    divisores = []
    
    for elemento in possiveis_divisores:
        if numero%elemento == 0:
            list.append(divisores,elemento)
    
    if divisores == []:
        return True
    
    else:
        return False