# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula e retorna o numero de palvras da frase"""
    r=str.rstrip(frase)
    l=str.lstrip(r)
    s=str.spli(l)
    return str.count(s)