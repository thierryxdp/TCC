def busca(p,matriz):
    """Função que dada uma matriz e um setor de pesquisa=p, retorna todos os funcionários desse setor"""
    """string,list--->list"""
    resposta=[]
    for f in range(len(matriz)):
        if matriz[f][2]==p:
            resposta+=matriz[f]
    return resposta