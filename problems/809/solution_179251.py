def intercala(lista1,lista2):
    ''' Função que unifica e organiza uma quantidade de dados de uma listas '''
    '''list e list -> list'''

    'entrada: L1 e L2 = saída L3'

    L3 = ([L1] + [L2])

    L1 = list(lista1)
    L2 = list(lista2)
    
    return L3