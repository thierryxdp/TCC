def fatorial(numero):
    """ Dado um número, calcula e retorna o fatorial 
    dele;
    int -> int"""
    i = 0
    lista = list(range(numero, 0, -1))
    resposta = 0
    while (i < len(lista - 1)):
        resposta = lista[i] * lista[i + 1]
        i += 1
    return resposta