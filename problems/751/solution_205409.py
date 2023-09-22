# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que dada uma frase, retorna o numero de palavras da frase; str->int
    Entrada=['frase']
    saida=['numero de palavras']"""
    return len(str.split(frase))