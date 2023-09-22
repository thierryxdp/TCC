def media_matriz(inteiros):
    """Função que dada uma matriz de numeros inteiros nao vazia, me retorna
a media de todos os numeros que estao nessa matriz, somente com duas casas decimais
 list--> float."""
    colunas = len(inteiros[0])
    linhas = len (inteiros)
    elementos = 0
    for i in range(len(inteiros)):
        elementos += sum(inteiros[i])
        quant_elementos = colunas*linhas
    media = elementos/quant_elementos
    return round (media,2)