def insere(lista_numero,n):
    """funcao que calcula e retorna uma lista de numeros na ordem crescente em que n(um numeto inteiro) deve ser colocado na posicao correta.
    ind,ind-->ind"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero