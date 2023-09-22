def insere(lista_numero, n):
    """Função que me dada uma lista ordenada, irá me retornar outra lista com o numero passado como parametro em sua
    respectiva posição na ordem, deixando a lista ainda no final de forma ordenada. list>list"""
    A=list.append(lista_numero,n)
    B=list.sort(lista_numero)
    return A+B