def insere(lista_numero, n):
    """Recebe uma lista e um numero. Adiciona n a lista_numero
    	e reordena a lista em orde crescente"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero