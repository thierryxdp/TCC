def soma_h(n):
    """função para calcular e retornar o valor h com n termos onde n é inteiro e dado como entrada 
    int -> float"""
    soma = 0
    x = list(range(1,n+1))
    for numero in x:
        if n == int(n):
            calculo = (1/numero)
            soma += calculo
    return round(soma,2)