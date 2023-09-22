def acima_da_media(lista):
    '''Função que dado uma lista com as notas dos alunos, retorna uma lista ordenando em ordem crescente todas as notas acima da média 
      list->list'''
    L=lista
    soma=sum(L)
    qnt=len(L)
    media=soma/qnt
    list.append(L,media)
    list.sort(L)
    indece=list.index(L,media)
    novo_indece=indece+1
    L=L[novo_indece:]
    if media==L[0]:
        return []
    else:
        return L