def busca(setor,matriz):
    '''funcao que receba uma matriz e realize uma busca por setor ou sej dado um de um s
setor da empresa, retorna os dados de todos os funcionários do setor
str,list->list'''
    lista=[]
    for contato in matriz:
        for area in contato:
            if area==setor:
                lista=[contato[0:2]+contato[3:]]+lista
    return lista