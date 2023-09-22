def filtraMultiplos (lista_numeros:list, n:int)->list:
    """recebe uma lista de numeros e um numero, e retorna outra lista 
    contendo todos os elementos da lista original que forem divisiveis por n"""
    i = 0
    lista = []
    while i < len(lista_numeros):
        if lista_numeros[i] % n == 0:
            lista.append(lista_numeros[i])
        i += 1
    return lista