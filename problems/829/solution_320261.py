def soma_h(N:int)->float:

    """ Dado a equação -> H = 1 + 1/2 + 1/3 ... + ... + 1/N
        Função que e retornar o valor da soma de frações com N termos (H)
    """
        
    soma_fracoes = 0

    for termo in range(1,(N+1)):

        H = 1/termo

        soma_fracoes = soma_fracoes + H

    return round(soma_fracoes,2)