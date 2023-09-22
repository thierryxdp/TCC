# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que dada uma frase, retorna o numero de palavras da frase, considerando que a frase pode ter espaços no inicio e no final.
    string -> int"""
    return len(str.split(frase))