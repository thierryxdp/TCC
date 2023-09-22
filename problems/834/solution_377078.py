def media_matriz(matriz):
    """Recebe uma matriz de inteiros não vazia e retorna a
       média de todos os elementos da matriz
       parâmetros de entrada:list(list)
       parâmetros de saída:float"""
    matriz=[]
    lista1=[]
    elemento=0
    soma=0
    for linha in matriz:
        for aij in linha:
            elemento=elemento+1
            list.append(lista1,aij)
        soma=sum(lista1)
    media=sum(lista1)/len(lista1)
    return media