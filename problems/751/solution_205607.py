# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna o numero de palavras que possui na frase. str->int"""
    frase1 = str.strip(frase)
    frase2 = str.join('-', str.split(frase1))
    frase3 = str.count(frase2, '-')
    return frase3