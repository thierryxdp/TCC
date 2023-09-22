def acima_da_media(lista_notas):
    '''Função que recebe uma lista com as notas dos alunos de uma turma e retorna outra lista contendo
    as notas dos alunos que ficaram acima da média.
    list - > list'''
    
    media = sum(lista_notas)/len(lista_notas)
    
    
    
    list.append(lista_notas, media)
    list.sort(lista_notas)
    
    indice = list.index(lista_notas, media)
    
    return lista_notas[indice:]