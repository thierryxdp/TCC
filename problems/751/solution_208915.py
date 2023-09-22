# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """faca uma funçao que dada uma frase, retorne o numero de palavras da frase.
    considere que a frase pode ter espaços no inicio e no final"""
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)