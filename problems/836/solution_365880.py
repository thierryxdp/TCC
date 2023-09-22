def busca(setor, matriz):
    '''Recebe o nome de um setor e uma matriz contendo os dados dos
    funcionários de uma empresa, no formato:

    [['Adalberto Ferreira', '1091982', 'Contabilidade', '(21)99281-2983'],
    ['Juliana Vasconcelos', '1111722', 'RH', '(21)99848−1902'],
    ['Flavia Amorim', '1128938', 'Contabilidade', '(22)99273-9404']]

    obs: cada linha da matriz tem quatro entradas, representando as
    informações referentes a nome, registro, setor e telefone de um
    funcionário, nesta ordem. O número de linhas depende da quantidade de
    funcionários. Todas as entradas da matriz estão em formato string.

    Retorna uma lista de listas das informações de todos os funcionários
    do setor dado (sem o nome do setor entre essas informações).

    str, list -> list'''

    qntFuncionarios = len(matriz)
    numColunas = len(matriz[0])

    pessoasSetor = []

    for i in range(qntFuncionarios):
        if setor in matriz[i]:
            infoPessoa = matriz[i][:]
            
            list.remove(infoPessoa, setor)
            
            list.append(pessoasSetor, infoPessoa)
            
    return pessoasSetor