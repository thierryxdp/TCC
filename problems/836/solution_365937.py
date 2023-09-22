def busca(setor,mat):
    '''funç˜ao que recebe uma string e uma matriz como a do exemplo e uma busca por setor,
       ou seja, dado o nome de um setor da empresa, a funç˜ao retorna uma lista com os
       dados de todos os funcionários daquele setor.
       str,list->list '''
    linhas=len(mat)
    colunas=len(mat[0])
    lista=[]
    lista2=[]
    for i in range(linhas):
        lista=[]
        for j in range(colunas):
            list.append(lista,mat[i][j])
            if setor in lista:
                list.append(lista2,lista)
    return lista2