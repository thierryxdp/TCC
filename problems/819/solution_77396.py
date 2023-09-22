def filtraMultiplos(lista_de_numeros, numero):
    '''retorna os numeros da lista fornecida que sao divisiveis pelo numero fornecido.
    list, int -> list'''
    divisiveis = []
    for elemento in lista_de_numeros:
        if elemento % numero == 0:
            divisiveis.append(elemento)
    return divisiveis