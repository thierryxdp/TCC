def quant_palavras(frase):
    '''Função que, dado como parâmetro uma frase no formato string, retorna a quantidade de palavras da frase; str - > int.'''
    palavras = str.split(frase)
    return len(palavras)