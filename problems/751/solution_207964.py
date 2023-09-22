# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Ao receber uma frase (entre aspas), retorna
    a quantidade de palavras nesta frase.
    str -> int"""
    frase = frase.strip()
    frase = frase.split(' ')
    return len(frase)