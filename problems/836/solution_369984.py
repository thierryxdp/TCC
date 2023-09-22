def busca(setor,matriz):
    '''
    Função que recebe uma matrize faça uma busca por setor,dado o nome do setor,e
    retorna os dados de todos os funcionários daquele setor;
    string,list(list) -> list(list)
    '''

    dados = []

    for dado in matriz:
        for info in dado:
            if setor in info:
                dados.append(dado)
    return dados