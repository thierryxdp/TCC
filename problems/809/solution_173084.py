def intercala(lista1, lista2):
    ''' Ao serem dadas como entrada duas listas de 3 elementos, a funcao re-
    torna uma terceira lista com os elementos das duas anteriores intercala-
    dos;
    
    Exemplo: 
        lista1 = [1,3,5]
        lista2 = [2,4,6]
        O retorno sera a lista [1,2,3,4,5,6] 
    
    list -> list '''
    
    return [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]