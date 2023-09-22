# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que tem de entrada uma frase, e reto,
    e retorna a quantidade de palavras presente nela"""
    
    x=frase.split()
    return len(x)