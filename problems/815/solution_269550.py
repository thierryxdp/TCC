def insere(lista_numero,n):
    """Função que insere o algarismo n em uma lista crescente,
na posição correta"""
    nova_lista = list.append(lista_numero,n)
    return list.sort(nova_lista)