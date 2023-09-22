def soma_h(n):
    """Essa função retorna a soma de um sequencia 1 ate 1/n"""
    """int->float"""
    i=0
    soma=0.0
    for i in range(1,n+1):
        soma=soma + 1/i
    return round(soma,2)