def busca (setor, matriz):
    """dado um setor e uma matriz na forma: Nome, registro, 
    setor e telefone do funcionário. A função retorna as informações
    (da matriz) de todos os funcionários daquele setor;
    list -> list"""
    matrizcerta = []
    lista = []
    resposta = []
    for x in matriz:
        if setor == x[2]:
            list.append(matrizcerta,x)
    for y in range(len(matrizcerta)):
        for z in matrizcerta[y]:
            if z != setor:
                list.append(lista,z)
    	list.append(resposta,lista)
    return resposta