# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """uma funcao que dada uma frase, retorna o numero de palavras da frase"""
    palavra = str.split(frase)
    return len(palavra)