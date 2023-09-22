def soma_h(n):
    """essa funcao calcula e retorna o valor H com N termos onde N e inteiro e dado com entrada"""
 	"""int-> float"""
    soma=0
    for i in range(1,n+1):
        soma=soma+(1/i)
    return round(soma,2)