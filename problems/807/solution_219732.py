def conta_frases(texto):
    """Funcao que calcula e retorna o número de frases 
    da string (texto) de entrada.
    str -> int"""

    lista1 = texto.split('?')
    string1 = "/".join(lista1)

    lista2 = string1.split('...')
    string2 = "/".join(lista2)

    lista3 = string2.split('.')
    string3 = "/".join(lista3)

    lista4 = string3.split('!')
    string4 = "/".join(lista4)

    lista_final = string4.split("/")
    
    quant_frases = len(lista_final) - 1

    return quant_frases