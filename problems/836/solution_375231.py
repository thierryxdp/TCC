def busca(setor,matriz):
    """Função que receba uma matriz e retorne, pela busca por setor, os dados
    de todos os funcionários daquele setor; str,list => tuple"""
    resultadi = []
    for linha in range(len(matriz)):
        if setor == matriz[linha][2]:
            list.remove(matriz[linha],setor)
            list.append(resultado,matriz[linha])
    return resultado