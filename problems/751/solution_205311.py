# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que dada uma frase, retorne o número de palavras da frase;
    string-> int"""
    var1 = str.split(frase)
    return len(var1)