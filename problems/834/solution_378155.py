# Dada uma matriz, queremos a média de seus elementos.
# Resolução:
# 1. Faz a média de todos os elementos de cada linha;
# 2. Soma todas as medias;
# 3. Divide a soma pelo número de colunas;
# 4. Retorna

def media_matriz(matriz: list) -> float:
    '''Dada uma matriz, retorna a média de seus elementos'''
    nlin = len(matriz)
    ncol = len(matriz[0])
    media1 = 0
    media = 0
    for linha in matriz:
        media1 += sum(linha) / ncol
    media = round(media1 / nlin, 2)
    return media