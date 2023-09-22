# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número de palavras de uma frase, str->int"""
    frase=str.split(frase," ")
    list(frase)
    return len(frase)