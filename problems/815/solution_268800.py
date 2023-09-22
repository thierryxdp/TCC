def insere(lista_numero,n):
    '''dados uma lista de números ordenadas de forma crescente e um número, retorna a lista atualizada com o número de forma crescente.'''
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero