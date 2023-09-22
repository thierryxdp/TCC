def filtraMultiplos(lista, numero):
    """Função que filtra os múltiplos de um número de uma lista de inteiros;
    list, int -> list"""
    contador = 0
    n_lista = []
    while contador<len(lista):
        if lista[contador]%numero == 0:
                 n_lista.append(lista[contador])
        contador+=1
    return n_lista