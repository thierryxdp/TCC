def insere(lista_numero, n):
    """Função que insere o número n na lista de ordem crescente de entrada.
    list[int],int-> list"""
    a1 = list.append(lista_numero,n)
    a2 = list.sort(a1)
    return a2