# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a string 's' com uma hashtag no inicio no meio e no final
    str -> str"""
    from math import ceil
    tamanho = len(s)
    metade_tamanho = int(floor(tamanho/2))
    nova_s = "#" + s[:metade_tamanho] + "#" + s[metade_tamanho:] + "#"
    return nova_s