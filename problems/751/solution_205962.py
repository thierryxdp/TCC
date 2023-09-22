# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A funcao recebe uma frase e retorne o numero de palavras da frase,
    Considerando que a frase pode ter espacos no inicio e no final."""
    n = str.count(frase,'')
    return n + 1