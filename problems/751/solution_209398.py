# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase(str), retorna a quantidade de palavras (int)"""
    return len(str.split(frase," "))