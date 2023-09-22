def media_matriz(matriz):
    ''' funcao que dada uma matriz retorna a media dos numeros da matriz com duas casas decimais de precisao. list --> float'''
    soma = 0
    quantidade = len(matriz)*len(matriz[0])
    for linha in matriz:
        soma += sum(linha)
    return round(soma/quantidade,2)