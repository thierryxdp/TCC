def eh_quadrada(matriz):
    "Função para verificar se uma matriz é quadrada ou não"
    l= 0
    c= 0
    for x in matriz:
           l += 1
           c = len(x)
    return l == c