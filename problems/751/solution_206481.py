# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funçao que retorna o numero de palavras de uma frase"""
    x = str.split(frase)
    return len(x)