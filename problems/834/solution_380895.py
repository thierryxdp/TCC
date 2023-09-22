def media_matriz(matriz):
    '''Essa função recebe uma matriz e retorna
    a média de todos os números dessa matriz, com duas casas decimais,
    list->float'''
    soma=0
    cont_elem=0 
    for n in matriz:
        soma+=sum(n)
        cont_elem+=len(n)
    return round(soma/cont_elem,2)