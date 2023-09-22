# Dada uma matriz, quer-se saber se é quadrada.
# Resolução:
# 1. Define o número de linhas da matriz;
# 2. Define o número de colunas da matriz;
# 3. Se a matriz for vazia ou tiver mesmo número de
#    linhas e colunas (quadrada), atribui bool True
# 4. Caso não, atribui bool False
# 5. Devolve o bool

def eh_quadrada(matriz: list) -> bool:
    '''Dada uma matriz, diz se é quadrada'''
    nlin = len(matriz)
    ncol = len(matriz[0])
    quadrada = ()
    if ((not(matriz)) or (nlin == ncol)):
        quadrada = bool(1)
    else:
        quadrada = bool(0)
    return quadrada