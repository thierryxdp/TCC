# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """a função conta a quantia de palavras numa frase. STR->INT"""
    palavras=frase.split()
    return len(palavras)