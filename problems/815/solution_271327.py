def insere(lista_numero, n):
    '''
    Recebe uma lista numérica qualquer e mais um número n qualquer.
    Insere a lista prévia em uma variável m. Insere o número n 
    em uma lista e esta lista na mesma variável n. Efetua a soma das
    listas e coloca elas em uma variável o. Por conseguinte, organiza
    a lista com a função sort. E retorna a lista organizada.
    list, int -> list
    '''
    m = lista_numero; n = [n]
    o = m + n
    list.sort(o)
    return o