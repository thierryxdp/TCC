# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    contagem=frase.split(' ')
    return len(contagem)