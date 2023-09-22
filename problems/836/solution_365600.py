def busca(setor,m):
    '''retorna os dados dos funcionarios do setor em questão
    str,list->list'''
    m1=[]
    for funcionario in m:
        if funcionario[2]==setor:
            list.remove(funcionario,funcionario[2])
          	list.append(m1,funcionario)
    return m1