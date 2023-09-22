def busca(p,matriz):
    """Função que dada uma matriz e um setor de pesquisa=p, retorna todos os funcionários desse setor"""
    """string,list--->list"""
    resposta=[]
    i=0
    for f in range(len(matriz)):
        if matriz[f][2]==p:
            resposta[i]=matriz[f][0],matriz[f][1],matriz[f][3]
    return resposta