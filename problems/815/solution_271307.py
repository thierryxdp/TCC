def insere(lista_numero, n):
    '''Recebe uma lista de numeros em ordem crescente e coloca o numero n posição correta
       list, int -> list'''
    lista_numero.append(n)
    return list.sort(lista_numero)