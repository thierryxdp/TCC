def soma_h(n):
    """Dado um número inteiro n, a função calcula a soma 1 + 1/2 + ... + 1/n com 2 casas decimais de precisão; int -> int/float"""
    
    lista_numeros = list(range(2, n+1))
    lista_fracoes = []

    for numero in lista_numeros:
        list.append(lista_fracoes,1/numero)
    return round(1 + sum(lista_fracoes), 2)