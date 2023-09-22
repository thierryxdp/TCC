def busca(setor,matriz):
    '''Recebe o nome de um setor da empresa (string) e uma matriz com as
    informações de todos os funcionários e retorna as informações dos 
    funcionários daquele setor; str -> list(list)'''
    informacoes_selecionadas = []
    for i in range(len(matriz)):
        informacoes_individuais = []
        if matriz[i][2] == setor:
            informacoes_individuais = [matriz[i][0]] + [matriz[i][1]] + [matriz[i][3]]
            list.append(informacoes_selecionadas,informacoes_individuais)
    if informacoes_selecionadas == []:
        return []
    else:
        return informacoes_selecionadas