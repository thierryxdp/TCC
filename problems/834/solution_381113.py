def media_matriz(matriz):
    'função que recebe uma matriz de inteiros, não vazia, retorna a média de '
    'todos os números com duas casas decimais. list->float'
    soma=0
    divisor=0
    n=0
    while n<len(matriz):
        soma+=sum((matriz)[n])
        divisor+=len((matriz)[n])
        n+=1
    return round(((soma)/(divisor)),2)