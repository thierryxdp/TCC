def soma_h(n):
    """Dada a função H definida como sendo a soma dos inversos do número
    1 ao número n, retorna a imagem de H com arredondamento de duas casas
    decimais;
    int->float"""
    soma=0
    for x in range(1,n+1):
        x=1/x
        soma+=x
    return round(soma,2)