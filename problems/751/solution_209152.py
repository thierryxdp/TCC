# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna a quantidade de palavas na frase de entrada
    str->int"""
    palavras=str.split(frase)
    return len(palavras)