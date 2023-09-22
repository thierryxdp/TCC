def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
            if palavra in matriz[:][i]:
                x=matriz[:][i]
                list.append(resposta,x)
                list.remove(x,palavra)
                resposta=resposta
    return resposta