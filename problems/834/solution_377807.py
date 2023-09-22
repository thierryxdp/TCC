# QUESTÃO 3 - OK!
def media_matriz(matriz):
    """ Dado uma matriz de inteiros vamos retormar a media de todos os numeros da matriz com duas casa deciamis de precisão.
        Parametros:
        Entrada -> matriz : list
        Saida   -> float   """
    m=matriz
    num_linha=len(m)
    num_coluna=len(m[0])
    total=num_linha*num_coluna
    soma=0
    for i in range(num_linha):
        for j in range(num_coluna):
            x=m[i][j]
            soma=soma+x
            media=soma/total
    return round(media,2)