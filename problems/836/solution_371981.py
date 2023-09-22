def busca(setor,matriz):
    '''retorna uma lista com todos os dados de um funcionario que trabalha
    em tal setor, dado uma matriz
    str,list->list'''
    lista=[]
    for sublista in matriz:
        for el in sublista:
            if el==setor:
                del sublista[2]
                lista=lista+[sublista]
    return lista