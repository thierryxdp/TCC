# Dada uma matriz, quer-se saber se é quadrada.
# Resolução:
# 1. Verifica se a matriz é vazia, caso sim atribui bool True;
# 2. Define o número de linhas da matriz;
# 3. Define o número de colunas da matriz;
# 4. Se a matriz tiver mesmo número de
#    linhas e colunas (quadrada), atribui bool True
# 5. Caso não, atribui bool False
# 6. Devolve o bool

def eh_quadrada(matriz: list) -> bool:
    '''Dada uma matriz, diz se é quadrada'''
    quadrada = bool()
    if (not(matriz)):
        quadrada = bool(1)
    nlin = len(matriz)
    ncol = len(matriz[0])
    if (nlin == ncol):
        quadrada = bool(1)
    else:
        quadrada = bool(0)
    return quadrada