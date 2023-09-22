# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase): 
    """A função conta o numero de palavras na frase dada como parâmetro.
string-->int"""
    s=str.split(frase)
    return len(s)