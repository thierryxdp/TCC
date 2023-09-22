def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    """dada uam lista de numeros e um int return---> lista"""
    ordenada= insere(lista_numero,n)
    return ordenada[list.index(ordenada,n)+1:]