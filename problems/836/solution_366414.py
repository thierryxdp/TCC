def busca(palavra,matriz):
    '''funcao que retorna todos os dados de uma lista na matriz
    caso a palavra dada na entrada se encontre nessa lista
    str,list->list'''
    resposta=[]
    for i in range(len(matriz)):
            if palavra in matriz[:][i]:
                lista=matriz[:][i]
                list.append(resposta,lista)
                list.remove(lista,palavra)
                resposta=resposta
    return resposta