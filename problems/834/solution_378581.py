def media_matriz(matriz):
    '''função que, dada uma matriz de inteiros nao vazia,
    reetorna a media de todos os numeros da matriz, com duas
    casas de precisao
    matriz -> float'''
    comp=0
    soma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return round(soma/comp,2)