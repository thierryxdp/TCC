def media_matriz(matriz):
    'função que recebe uma matriz de inteiros, não vazia, retorna a média de '
    'todos os números com duas casas decimais. float->float'
    soma=0
    n=0
    for proximo in matriz:
        soma+=proximo
        n+=1        
    return soma/n