def acima_da_media(lista):
    '''Função que dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima da média
    list -> list'''
    
    media = sum(lista) / len(lista)
    
    list.append(lista, media)
    
    list.sort(lista)
    
    a = list.index(lista, media)
    
    return lista_numeros[a+1:]