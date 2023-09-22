def soma_h(n):
    """Retorna o valor H com N termos.int-->float"""
    i=n
    soma=0
    while i>0:
        numero=1/i
        soma=soma+numero
    	i=i-1
    return round(soma,2)