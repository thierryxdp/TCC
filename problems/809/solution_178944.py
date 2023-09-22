def intercala(lista1, lista2):
    """Define uma função que dada duas listas gera uma terceira que se forma intercalando os elementos das duas primeiras listas"""
    lista3 =[]
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3