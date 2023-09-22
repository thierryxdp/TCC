def repetidos(lista):
    lista_numeros_unicos = []
    for numero in lista:
        if(lista[lista.index(numero)] == lista[lista.index(numero)-1]):
            lista_numeros_unicos.append(numero)
        else:
            pass
    return len(lista_numeros_unicos)