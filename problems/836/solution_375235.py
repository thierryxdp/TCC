def busca(setor,matriz):
    """Função que receba uma matriz e retorne, pela busca por setor, os dados
    de todos os funcionários daquele setor; str,list => tuple"""
    v = []
    for l in range(len(matriz)):
        if setor == matriz[l][2]:
            list.remove(matriz[l],setor)
            list.append(v,matriz[l])
    return v