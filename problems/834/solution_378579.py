def media_matriz(matriz):
    """dada uma matriz int e nao vazia, retorna a media dos numeros da matriz"""
    comp=0
    soma=0
    for i in matriz:
        comp=comp+len(i)
        soma=soma+sum(i)
    return round(soma/comp, 2)