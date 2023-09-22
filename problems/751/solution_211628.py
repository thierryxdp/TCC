# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase, retorna a quantidade de palavras
    da mesma.
    assinatura: string -> int"""
    return len(str.split(frase))