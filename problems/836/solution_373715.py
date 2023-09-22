def busca(matriz,setor):
    '''retorna as informações dos funcionarios de determinado setor; list,str->list'''
    inf=[]
    for i in matriz:
        for j in i:
            if j==setor:
                i.remove(j)
                inf+=i
    return inf