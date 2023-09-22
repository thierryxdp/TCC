def filtraMultiplos(lista,numero):
    """Funcao que retorna todos os elementos contidos em 'lista' que sao divisiveis pelo 'numero';
    list, int -> list"""
    divisiveis = []
    elemento = 0
    while elemento < len(lista):
        if lista[elemento]%numero == 0:
            divisiveis += (lista[elemento],)
        elemento += 1
    return divisiveis