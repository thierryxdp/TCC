def busca(setor,matriz):
    """Essa funcao recebe a matriz e o setor da empresa e retorna os contatos na matriz que participam deste setor
    str , list -> list"""
    resultado_busca = []
    for i in range (len(matriz)):
        if setor in matriz[i]:
            matriz[i].pop(2)
            resultado_busca.append(matriz[i])
    return resultado_busca