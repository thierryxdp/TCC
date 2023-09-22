def insere(lista_numero, n):
    """Função que me dada uma lista ordenada, irá me retornar outra lista com o numero passado como parametro em sua
    respectiva posição na ordem, deixando a lista ainda no final de forma ordenada. list.int>list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero