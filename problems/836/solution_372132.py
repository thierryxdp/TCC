def busca(setor,matriz):
    '''Recebe o nome de um setor da empresa (string) e uma matriz com as
    informações de todos os funcionários e retorna as informações dos 
    funcionários daquele setor; str -> list(list)'''
    informacoes_selecionadas = []
    for i in range(len(matriz)):
        if matriz[i][2] == 'Contabilidade':
            list.append(informacoes_selecionadas,matriz[i])
    return informacoes_selecionadas