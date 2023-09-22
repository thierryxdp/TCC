# Função que dada uma frase retorna o número de palavras da frase
# frase= Frase que será posta no def
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase retorna o número de palavras da frase str-->int"""
    frase = str.split(frase)
    return len(frase)