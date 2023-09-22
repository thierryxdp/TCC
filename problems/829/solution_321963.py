def soma_h (n):
    """Funcao para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada. Retorne seu resultado somente com 2 casas decimais, utilizando a função round(numero, 2).
    int -> float"""
    soma = 0
    indice = 0
    while indice < len(lista1):
        x=(lista2[indice])/factorial(lista1[indice])
        if indice % 2 ==0:
            soma = soma + x
        else:
            soma = soma - x
        indice+=1
    return round (soma,2)