# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Determina quantas palavras tem em uma  frase; str ==> int """
    nova_frase= frase.split()
    quant = len(nova_frase)
    return quant