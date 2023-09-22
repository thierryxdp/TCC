def total(lista,produtos):
    """ - """

    x = 0
    contador = 0
    
    while contador != len(lista):
        if lista[contador] in produtos:
            x = x + produtos[lista[contador]]
        contador += 1

    resposta = round(x,2)
    
    return resposta