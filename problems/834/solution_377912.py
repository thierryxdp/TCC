def media_matriz(matriz):
    """Função que dada uma matriz, retorna a média de todos os números da matriz com 
       precisão de duas casas decimais.
       list->float"""
    qnt_n = 0
    soma = 0
    media = 0
    for linha in range(0,len(matriz)):
        for coluna in range(0,len(matriz[linha])):
            qnt_n = qnt_n + 1
            soma = soma + matriz[linha][coluna]
            media = soma / qnt_n
    return round(media,2)