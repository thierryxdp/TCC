def insere(lista_numero,n):
    'Função q insere número em uma lista e retorna em ordem crescente'
    'List -> List'
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero