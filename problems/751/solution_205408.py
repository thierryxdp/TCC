# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase, a função retorna o número de palavras dessa frase;
    str --> int"""
    a = str.split(frase)
    b = len(a)
    return b