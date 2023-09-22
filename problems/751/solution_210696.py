# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o numero de palavras existentes na frase inserida 
    na função"""
    s = str.split(frase, )
    r = str.count(s, s[:])
    return r