def busca(NomeSetor, matriz):
    """função que dados um nome do setor e uma matriz, retorna os dados de todos os funcionários daquele setor;str,list-->list"""
    buscados=[]
    for funcionarios in matriz:
        if NomeSetor in funcionarios[3]:
            buscados.append(buscados[:2]+funcionarios[3:])
    return buscados