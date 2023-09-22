# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função recebe uma frase e retorna o número de palavras dela"""
    x=frase
    y=x.split()
    return len(y)