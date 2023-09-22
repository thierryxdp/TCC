def media_matriz(matriz:list)->float:
    """dada uma matriz de inteiros n˜ao vazia, retorna a média
de todos os números da matriz, com exatamente duas casas decimais de precis˜a"""
    soma=0
    total=0

    for i in matriz:
        for j in i:
            soma=soma+j
        total=total+len(i)
    return round(soma/total,2)