5# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase, retorna o npumero de palavras dessa frase.
    str -> int"""
    s=str.split(frase)
    return len(s)