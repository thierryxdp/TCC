def insere(lista_numero, n):
    '''Recebe uma lista de numeros em ordem crescente e coloca o numero n posição correta
       list, int -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero