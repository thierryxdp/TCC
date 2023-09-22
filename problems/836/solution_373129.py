def busca(setor,matriz):
    '''função que retorna uma sublista que contém uma string dentro da matriz; matriz => list'''
    resposta=[]
    for area in matriz:
        if area[2]==setor:
            list.append(resposta,area[:2]+area[3:])
    if resposta!=[]:
        return resposta
    return []