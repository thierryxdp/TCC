# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o numero de palavras contidas numa frase"""
    """str - > int"""
    k = str.split(frase,' ')
    return len(k)