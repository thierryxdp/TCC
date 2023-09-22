# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Pede uma frase qualquer de entrada e conta o número
    de palavras nessa frase.
    string->int"""
    palavras=str.split(frase)
    return len(palavras)