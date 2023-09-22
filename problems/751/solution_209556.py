# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """mostra a quantidade de palavras presente numa frase"""
    palavras=list(frase.split(' '))
    return len(palavras)