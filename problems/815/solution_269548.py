def insere(lista_numero,n):
    """Função que insere o algarismo n em uma lista crescente,
na posição correta""" #insert e sort
    nova_lista = list.append(lista_numero,n)
    lista_cresc = list.sort(nova_lista)
    return lista_cresc