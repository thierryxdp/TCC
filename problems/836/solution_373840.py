def busca(setor, dados):
    '''Dado um setor e uma matriz com os dados dos funcionarios de uma empresa,
    retorna uma lista com as informaçoes dos funcionarios daquele setor;
    list -> list'''

    encontrados = []

    for i in range(len(dados)):
        if dados[i][2] == setor:
            list.append(res, [dados[i][0], dados[i][1], dados[i][3]])

    return encontrados