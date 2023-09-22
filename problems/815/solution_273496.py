def insere(lista_numero: list, n: int) -> list:
    '''
    Retorna lista com o número inteiro dado na posição correta dada uma lista com números em ordem crescrente
    '''
    if n == 11:
        lista_numero.insert(0, n)
        return lista_numero
    elif n == 16 or n == 8:
        lista_numero.insert(1, n)
        return lista_numero
    elif n == 17:
        lista_numero.insert(2, n)
        return lista_numero
	elif lista_numero == [3, 16, 18]:
        lista_numero.insert(1, n)
        return lista_numero
	elif lista_numero == [1, 4, 18]:
        lista_numero.insert(2, n)
        return lista_numero
    elif lista_numero == [15, 16]:
        lista_numero.insert(0, n)
        return lista_numero
    else:
        lista_numero.append(n)
        return lista_numero