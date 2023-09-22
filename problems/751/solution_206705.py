# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase, retorna o número de palavras da frase, str--> int"""
    tira_espacos = str.split(frase)
    return len(tira_espacos)