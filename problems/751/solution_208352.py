# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    frase = str.split(frase)
    return len(frase)
    """A função recebe uma frase (frase) e retorna a quantidade
    de palavras através da função len, considerando que possa ter
    espaços tanto no início quanto no fim."""