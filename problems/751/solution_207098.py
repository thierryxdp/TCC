# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que dada uma frase, retorne a quantidade de palavras que a frase possui; string -->int"""
    frase= frase.strip()
    frase= frase.split()
    return len(frase)