def acima_da_media(lista):
    '''
       Função que recebe uma lista com as notas dos alunos de uma turma 
       e retorna uma lista ordenada com as notas que ficaram acima de média
       list -> list
    '''
    media=sum(lista)/len(lista)
    list.insert(lista,1,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    
    if list.count(lista,media)>=2:
        return lista[posicao+2:]
    else:
        return lista[posicao+1:]