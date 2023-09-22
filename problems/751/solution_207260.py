def quant_palavras(frase):
    """Funcao que dado o parametro de entrada frase retorna
    o numero de palavras da frase dada. A frase pode ter 
    espacos no inicio e no final;
    str->int"""
    return len(str.split(frase))