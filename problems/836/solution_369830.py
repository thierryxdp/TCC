def busca(setorempresa,mat):
    '''funcao que retorna os dados de todos os funcionarios
    de um setor; str,list->list'''
    f=0
    soma=[]
    for f in range(len(mat)):
        if setorempresa in mat[f]:
            del mat[f][2]
            soma=soma+[mat[f]]
    return soma