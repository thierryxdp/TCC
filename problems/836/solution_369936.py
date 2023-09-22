def busca(setor, matriz):
    '''avalia e retorna uma lista com os dados de todos
    os funcionarios do setor a ser buscado
    str, list-> list'''
    resultados=[]
    for funcionario in matriz:
        test=funcionario.copy()
        for dado in funcionario:
            if dado==setor:
                test.remove(dado)
                resultados+=[test]
    return resultados