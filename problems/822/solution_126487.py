def repetidos(lista):
    lista_numeros_unicos = []
    for numero in lista:
        if(lista.count(numero) > 1):
            lista_numeros_unicos.append(numero)
        else:
            pass
    return len(lista_numeros_unicos)/2