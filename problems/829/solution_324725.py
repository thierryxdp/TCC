def soma_h(n):
    """função que calcula e retorna o valor H com N termos onde N é inteiro e dado como entrada"""
    soma=0
    for x in range(1,n+1):
        soma+=1/x
    return round(soma,2)