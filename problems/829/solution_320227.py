def soma_h(n):
    """Função que calcula e retorna o valor H com N termos onde N e inteiro
       Retornar o resultado com apenas duas casas decimais
       int -> float"""
    lista = list(range(n+1))
    del lista[0]
    soma = 0
    for cadaN in lista:
        cadaN = 1/cadaN
        soma = soma + cadaN
    return round(soma,2)