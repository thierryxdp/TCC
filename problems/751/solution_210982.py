# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Essa função determina quantas palavras existem em uma frase.
    string -> int"""
    frase = str(frase)
    lista1 = frase.split(' ')
    return len(lista1)