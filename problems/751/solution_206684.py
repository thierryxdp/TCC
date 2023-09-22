# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao q retorna o numero de palavras dadas na frase
    levando em consideracao os espacos"""
    num = str.split(frase)
    return len(num)