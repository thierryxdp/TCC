def insere(li
    
def insere(lista_numero, n):
    """
    Dada uma lista numérica, adiciona um número n e reorganiza
    a lista colocando o n em uma posição de acordo com o seu
    valor.
    list, int -> list
    """
    list(lista_numero)
    lista_numero.append(n)
    listaOrganizada = list.sort(lista_numero)

    return listaOrganizada