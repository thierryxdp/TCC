def busca (setor, matriz):
    """dado um setor e uma matriz na forma: Nome, registro, 
    setor e telefone do funcionário. A função retorna as informações
    (da matriz) de todos os funcionários daquele setor;
    list -> list"""
    matrizcerta = []
    listasemsetor = []
    resposta = []
    for x in matriz:
        if setor == x[2]:
            matrizcerta = matrizcerta + [x]
    for y in range(len(matrizcerta)):
        for z in matrizcerta[y]:
            matrizcerta[y] = []
            if z != setor:
                list.append(matrizcerta[y],[z])
    return matrizcerta