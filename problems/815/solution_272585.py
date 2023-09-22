def insere(lista_numero, n):
    """Dada uma lista numérica, adiciona um número n e reorganiza a lista colocando o n em uma posição de acordo com o seu
    valor em módulo.
    list,int-->list"""
    list(lista_numero)
    lista_numero.append(n)
    listasorted = sorted(lista_numero)
    return listasorted