def busca(p,matriz):
    """Função que dada uma matriz e um setor de pesquisa=p, retorna todos os funcionários desse setor"""
    """string,list--->list"""
    resposta=[]
    i=0
    for f in range(len(matriz)):
        if matriz[f][2]==p:
            resposta[i]=matriz[f]
            i+=1
    return resposta