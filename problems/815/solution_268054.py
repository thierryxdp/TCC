def insere(lista_numero, n):
    """Função que insere o número n na lista de ordem crescente de entrada.
    list[int],int-> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero