def soma_h(n):
    """Função que calcula e retorna o valor H com N termos onde N é inteiro e dado como entrada; int -> int"""
    lista = range(n+1)
    soma = 0
    
    for count in lista:
        if count != 0:
            soma = soma + 1/count
    return round(soma,2)