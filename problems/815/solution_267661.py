def insere(lista_numero , n):
    """ funcao ira receber uma lista ordenada de numeros e ao receber um numero n ira inserir este em seu devido lugar mantendo a lista em ordem crescente
    entrada: list, int
    saida: list"""
    list.append (lista_numero,n)
    list.sort (lista_numero)
    return lista_numero