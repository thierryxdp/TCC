# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase, retorne o numero de palavras da frase.
    Dados de entrada: str
    Dados de saida: int"""
    return len(str.split(frase))