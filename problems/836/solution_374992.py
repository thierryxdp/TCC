def busca(setor, matriz):
'''recebe o setor de uma empresa e a matriz e retorna os dados de 
todos funcionarios desta'''
    resultado = []
    for i in matriz:
        if setor in i[2]:
            list.append(resultado, i)
            del resultado[-1][2]
    return resultado