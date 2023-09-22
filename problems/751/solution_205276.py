def quant_palavras(frase):
    '''Dada uma frase, a função retorna a quantidade de palavras nela. 
    srt -> int'''
    # (I) gerando uma lista com todas as palavras
    lista = str.split(frase) #OBS: como a pontuação sempre esta colada com a palavra antecedente, não impacta na conta.
    # (II)contando as palavras da frase a partir da lista
    quantidade_de_palavras = len(lista)
    return quantidade_de_palavras