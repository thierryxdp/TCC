# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao calcula e retorna quantas palavras tem em uma frase; string-->int"""
    frase=str.split(frase)
    return len(frase)