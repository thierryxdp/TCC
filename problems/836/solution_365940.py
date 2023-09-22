def busca(setor,mat):
    '''funç˜ao que recebe uma string e uma matriz como a do exemplo e uma busca por setor,
       ou seja, dado o nome de um setor da empresa, a funç˜ao retorna uma lista com os
       dados de todos os funcionários daquele setor.
       str,list->list '''
    cont=[]
    for i in range(len(mat)):
     if setor in mat[i][2]:
         del(mat[i][2])
         cont.append(mat[i])
    return cont