def busca(setor,m):
    '''retorna os dados dos funcionarios do setor em questão
    str,list->list'''
    i=0
    m1=[]
    for funcionario in m:
        if funcionario[2]==setor:
            list.append(m1,funcionario)
            del m1[i][2]
        i=i+1   
    return m1