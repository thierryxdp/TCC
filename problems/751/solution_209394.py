# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna o número de palavras de uma frase. int->string"""
    frase=str.split(frase)
    return len(frase)