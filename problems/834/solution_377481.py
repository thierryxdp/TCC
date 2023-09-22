def media(matriz):
    """Funcao que, dada uma matriz de inteiros, retorna a média de todos os numeros da matriz com duas casas decimais
    list -> float"""
    elementos=len(matriz)*len(matriz[0])
    soma=0
    for a in range(len(matriz)):
        soma=soma+sum(matriz[a])
    return round(soma/elementos,2)