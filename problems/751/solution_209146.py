# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase como entrada retorna o numero de palavras da frase.
    A frase pode ter espaços no início e no final.
    str->int"""
    x=len(frase.split())
    return x