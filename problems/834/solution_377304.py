def media_matriz(matriz):
    '''soma os valores de uma matriz e retorna a média dos números;list->float'''
    resposta=[]
    for i in matriz:
        soma= (sum(i))/len(i)
        list.append(resposta,soma)
    return round(sum(resposta)/len(resposta),2)