def busca(setor, matriz):
    '''avalia e retorna uma lista com os dados de todos
    os funcionarios do setor a ser buscado
    str, list-> list'''
    resultados=[]
    for funcionario in matriz:
        if funcionario[2]==setor:
            test=funcionario.copy
            test.remove(setor)
            resultados+=[test]
    return resultados