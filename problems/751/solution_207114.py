# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Essa função calcula a quantidade de palavras numa frase.
str -> int"""
    y = frase.strip()
    z = y.split(" ")
    return len(z)