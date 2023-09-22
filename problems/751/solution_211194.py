# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""def quant_palavras(frase):
    """Conta a quantidade de palavras em uma frase, str->int"""
    frase = str.split(frase)
    return len(frase)