def eh_ordenada(lista):
    '''Função que, dada uma lista contendo uma quantidade de valores numéricos,
        retorne se a lista está ordenada em ordem crescente, decrescente ou
        não odernada. A retorno da função deve ser uma Tupla onde o primeiro
        elemento é True, caso a lista esteja ordenada e False caso o contrário.
        O segundo elemento deve ser uma string "crescente", "decrescente" ou
        "desordenada", indicando como a lista encontra-se.
        Entrada: lista(int) ; Return: tupla(bool, str)'''
    lista2 = lista[:]
    lista.sort( )
    
    if lista2 == lista:
        return True, "crescente"

    elif lista2 == lista[::-1]:
        return True, "decrescente"

    else:
        return False, "desordenada"