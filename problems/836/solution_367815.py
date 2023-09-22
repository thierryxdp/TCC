def busca(nome,matriz):
    """ essa função visa buscar os dados de todos os funcionarios em certo setor da empresa
entrada -> str, list
saida -> list """
    resultado = []
    for i in range(len(matriz)):
        if nome in matriz[i]:
            resultado += matriz[i]
    return resultado