# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma frase e retorna a quantidade de palavas qie ela tem."""
    """(frase) => quantidade de palavras"""
    frase = (str.split(frase))
    return len(frase)