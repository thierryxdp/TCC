def busca(setor, matriz):
    """função que dados um nome do setor e uma matriz, retorna os dados de todos os funcionarios daquele setor;str,list-->list"""
    buscados=0
    for funcionario in matriz:
        if setor in funcionario[2]:
            buscados.append(funcionario[:2]+funcionario[3:])
    return buscados