def soma_h(num):
    """a função calcula e retorna o valor h com n termos onde n é int e
    dado como entrada;
    int->int"""
    soma = 0
    for i in range(1,num + 1):
        soma = soma + 1/i
    return round(soma,2)