def acima_da_media(lista_de_numeros):
    
    '''dada uma lista de números e um número qualquer n, 
    retorna o valor n em seu respectivo local na lista
    e remove os números menores '''
    n = 5
    list.append(lista_de_numeros, n)
    list.sort(lista_de_numeros)
    x = list.index(lista_de_numeros, n)
    y = len(lista_de_numeros) 
    
    return lista_de_numeros[x+1:y]