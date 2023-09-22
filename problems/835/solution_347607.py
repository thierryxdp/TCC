def melhor_volta(m):
    """função que recebe um matriz 6x10"""
    linhas = range(len(m))
    menor = []
    for i in linhas:
        menor = menor + [min(m[i])]
        jogador = list.index(menor,min(menor))
    return menor,jogador