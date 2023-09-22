def freq_palavras(frases):
    '''Funcao que retorna a quantidade de vezes em que uma palavra aparece em certa
frase de entrada, em formato de dicionario.
Str -> Dict'''
    lista_palavras = frases.split
    quant_palavras = {} 
    for palavra in list(lista_palavras):
        if palavra in quant_palavras:
            quant_palavras[palavra] += 1
        else:
            quant_palavras.update({palavra: 1})
    return quant_palavras