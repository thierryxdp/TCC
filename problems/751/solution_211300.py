# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna a quantidade de palavras que tem em uma frase"""
    x = frase.split(' ')
    return len(x)