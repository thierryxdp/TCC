def insere(lista_numero,n):
    """Função que dada uma lista ordenada e um inteiro n, inclui n na posição
    correta de modo que continue ordenada;list,int-->list"""
    if n not in lista_numero:
        list.sort(lista_numero)
        return list.append(lista_numero,n)