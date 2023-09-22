def busca(setor,matriz):
    """Dado um setor a função retorna todos os funcionários desse setor e suas informações
    str,list==>list"""
    funcionarios=[]
    for dados in range(len(matriz)):
        if matriz[dados][2]==setor:
            list.remove(matriz[dados],setor)
            list.append(funcionarios,matriz[dados])
    return funcionarios