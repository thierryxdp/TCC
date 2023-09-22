def busca(setor,m):
    '''retorna os dados dos funcionarios do setor em questão
    str,list->list'''
    m1=[]
    for funcionario in m:
        if funcionario[2]==setor:
            list.append(m1,funcionario)
            del m1[funcionario][2]
    return m1