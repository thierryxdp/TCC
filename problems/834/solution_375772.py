def media_matriz(m):
    '''Função que dada uma matriz(m) de inteiros não vazia, retorna a média de todos os números da matriz.
       parâmetros de entrada:list
       valor de retorno:float'''
    somas=[]
    for i in m:
        for j in i:
            list.append(somas,j)
    return round(sum(somas)/len(somas),2)