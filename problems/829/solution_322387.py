def soma_h(n): 
    """Retorna o valor H com n termos, de acordo com a expressão fornecida
       no enunciado. int-> float"""
    soma = 0
    for a in range(1,n+1):
        soma = soma + (1/a)
    return round(soma,2)