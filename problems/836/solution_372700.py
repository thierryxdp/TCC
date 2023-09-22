def busca (setor, matriz):
    """dado um setor e uma matriz na forma: Nome, registro, 
    setor e telefone do funcionário. A função retorna as informações
    (da matriz) de todos os funcionários daquele setor;
    list -> list"""
    setorcerto = []
    listasemsetor = []
    resposta = []
    for x in matriz:
        if setor == x[2]:
            setorcerto = setorcerto + [x]
    for y in setorcerto:
            for z in y:
                if z!= setor:
                    listasemsetor = listasemsetor + [z]
    resposta = resposta + listasemsetor
    return [resposta]