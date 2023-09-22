def filtraMultiplos(lista_de_numeros, numero):
    divisiveis = []
    for elemento in lista_de_numeros:
        if elemento % numero == 0:
            divisiveis.append(elemento)
    return divisiveis