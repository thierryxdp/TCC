def insere(lista_numero,n):
    """Função que ordena uma lista de números, sendo que na entrada ela recebe uma lista de números e um unico
    número e na saida ela devolve uma lista com esse numero inserido na lista e deforma ordenada"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero