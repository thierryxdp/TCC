def busca(setor,matriz):
    '''Recebe uma string com o setor e uma matriz com as informações dos funcionários'''
    dados = []
    for x in matriz:
        if x[2] == setor:
            list.append(dados,x[:2] + x[3:])
    if dados != []:
        return dados
    return []