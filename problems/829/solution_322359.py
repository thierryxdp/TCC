def soma_h(n):
    """Função que retorna a soma dos inversos dos inteiros até o número n
    inserido (arredondamento de duas casas decimais).
    int->float"""
    soma=0
    for i in range(1,n+1):
        soma=soma+(1/i)
    return round(soma,2)