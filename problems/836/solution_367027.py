def busca(setor,matriz):
    '''A partir de uma matriz, busca por um setor e retorna os funcionarios de tal setor
       parameters:
       setor: setor de trabalho
       matriz: matriz com o perfil de funcionarios
       str,list->list'''
    lista=[]
    for i in range(len(matriz)):
        if matriz[i].count(setor) > 0:
            del matriz[i][2]
            lista+=[matriz[i]]
            i+=0
    return lista
    if matriz[i].count(setor)==0:
        return lista