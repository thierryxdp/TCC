def acima_da_media(lista_de_numeros):
    
    '''dada uma lista de números 
    retorna os valores acima de 5 em seu respectivo local na lista
    e remove os números menores 
    int --> int '''
    
    n = 5
    list.append(lista_de_numeros, n)
    list.sort(lista_de_numeros)
    x = list.index(lista_de_numeros, n)
    y = len(lista_de_numeros) 
    
    return lista_de_numeros[x+1:y]