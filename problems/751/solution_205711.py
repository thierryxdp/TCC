# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função recebe uma frase, separa as palavras com base nos espaços em branco, coloca todas as palavras numa lista e calcula o número de itens na lista, ou seja, o número de palavras. A função recebe uuma str e retona um int"""
    palavras = frase.split()
    numero_de_palavras = len(palavras)
    return numero_de_palavras