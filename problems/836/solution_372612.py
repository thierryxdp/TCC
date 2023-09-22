def busca(setor,dados_funcionarios):
    '''Retorna os dados de todos os funcionários do setor buscado.
    str,list(list)->list(list)'''
    resultado_busca=[]
    for funcionario in dados_funcionarios:
        if funcionario[2]==setor:
            dados_fornecidos=funcionario[:]
            del dados_fornecidos[2]
            list.append(resultado_busca,dados_fornecidos)
    return resultado_busca