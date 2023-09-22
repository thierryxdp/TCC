# quantidade de palavras 
def quant_palavras(frase):
    """Funcao que retorna o numero de palavras contidas em uma frase, 
       a frase pode conter espaços entre as palavras ou nao. 
       str--> int"""
    return len(str.split(frase))