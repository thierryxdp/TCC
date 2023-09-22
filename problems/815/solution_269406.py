def insere(lista_numero, n):
    
    """Funçao que dada uma lista de números inteiros, inclue um número n e reorganiza a lista colocando o n em uma posição de acordo com o seu
    valor. 
    list, int, list"""
    list(lista_numero)
    lista_numero.append(n)
    listaOrdenada = sorted(lista_numero)

    return listaOrdenada