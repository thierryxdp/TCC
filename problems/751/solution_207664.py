# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase, retorna o número de palavras da mesma
    considerando possíveis espaços no início e no final"""
    frase = str.split(frase)
    return len(frase)