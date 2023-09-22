def soma_h(n):
    """ Função que calcula e retorna o valor H com N termos
    """
    
    valordeh = []
    soma = 0
    
    for i in range(1,n+1):
        valordeh.append(i)
        
    for elem in valordeh:
        numeros = 1/elem
        soma += numeros
        
    return round(soma, 2)