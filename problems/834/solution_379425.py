def media_matriz(matriz):
    '''funcao que recebe uma matriz de inteiros nao vazia
    retorna a media de todos os numeros da matriz arredondada
    para 2 casas decimais
    list->float'''
    numero_de_elementos=len(matriz)*len(matriz[0])
    somas=[]
    for linhas in matriz:
        list.append(somas,sum(linhas))
    return round((sum(somas)/numero_de_elementos),2)