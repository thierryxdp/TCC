def eh_quadrada(matriz):
    """Determinar como verdadeiro o numero de linhas que seja igual ao numero de colunas da matriz;
    list -> bool"""
    resultado = False
    tamanho_linha = len(matriz)
    if tamanho_linha <= 0:
        resultado = True
    else:
        tamanho_coluna = len(matriz[0])
        if tamanho_coluna == tamanho_linha:
            resultado = True
    return resultado