def quant_palavras(frase):
    """ Dada uma frase, que deve ser inserida entre aspas, retorna o número de
        palavras que há nessa frase """
    s = str.split(frase)
    numPalavras = len(s)
    return numPalavras