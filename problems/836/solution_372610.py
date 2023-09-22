def busca(setor,dados_funcionarios):
    '''Retorna os dados de todos os funcionários do setor buscado.
    str,list(list)->list(list)'''
    resultado_busca=[]
    for funcionario in dados_funcionarios:
        if funcionario[2]==setor:
            list.append(resultado_busca,funcionario)
    return resultado_busca