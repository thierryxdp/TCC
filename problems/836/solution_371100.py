def busca(setor, matriz):
    '''Dado o nome do setor e uma lista (matriz) com as informações dos funcionarios,
    retorna as informações do funcionarios daquele setor;
    str,list-> list'''

    funionarios = []

    for setor_buscado in range(len(matriz)):
        if str.lower(setor) in str.lower(matriz[setor_buscado][2]):
            list.append(funionarios,matriz[setor_buscado])
            list.remove(funionarios[setor_buscado-1],setor)

    return funionarios