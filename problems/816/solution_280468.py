def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    """retorna os numeros maiores que n numa lista. LIST(INT),INT->LIST(INT)"""
    ordenada= insere(lista_numero,n)
    return ordenada[list.index(ordenada,n)+1:]