def acima_da_media(lista):
    '''
    função que recebe uma lista com as notas dos alunas e 
    retorna as qie estão acima da média
    '''
    list.sort(lista)
    a = len(lista)
    b = list.index(lista,5,)
    
    return lista[b:a]