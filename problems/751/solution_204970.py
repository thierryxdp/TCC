# 
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase, retorna o numero de palavras na frase
    string -> int"""
    x = str.count(frase,' ',1,-1)
    return: (x+1)