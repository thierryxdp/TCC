def busca(palavra,matriz):
    resposta=[]
    for i in range(len(matriz)):
            if palavra in matriz[:][i]:
                lista=matriz[:][i]
                list.append(resposta,lista)
                list.remove(lista,palavra)
                resposta=resposta
    return resposta