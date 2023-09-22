def insere(lista_numero,n):
    """função recebe como entrada uma lista de numeros e um n e coloca ordenado com a função sorted"""
    lista_numero.append(n)
    listax = sorted(lista_numero)
    return listax