#list->float,int
def media_matriz(matriz):
    "Função que dada uma matriz retorna a média dos elementos dessa matriz."
    soma = 0
    for i in range(len(matriz)):
        soma=soma+sum(matriz[i])
        elem=len(matriz)*len(matriz[0])
    total= soma/elem
    return round(total,2)