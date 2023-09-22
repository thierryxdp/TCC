# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna o o numero de palavras contidas em uma determinada frase"""
    return str.count(str.strip(frase),' ')+1