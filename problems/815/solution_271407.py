def insere(lista_numero,n):
    ''' Função que recebe uma lista "lista_numero" e um inteiro "n", e retorna
    uma lista nova contendo n em ordem crescente'''
    ''' list, int -> list'''
    #casos de teste:
    ''' insere([6,5,4,767,5645,343],768) -> [4, 5, 6, 343, 767, 768, 5645]
        insere([290,84,43,2],5) -> [2, 5, 43, 84, 290]
        insere([5,8,2,3,100],98) -> [2, 3, 5, 8, 98, 100] '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero