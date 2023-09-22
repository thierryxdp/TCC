def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase
    str->int"""
    palavras_separadas=frase.split()
    palavras_lista=list(palavras_separadas)
    qnt_palavras=len(palavras_lista)
    return qnt_palavras