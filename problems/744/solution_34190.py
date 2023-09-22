def hashtag(s):
    """Retorna a string 's' com uma hashtag no inicio no meio e no final
    str -> str"""
    from math import floor
    tamanho = len(s)
    metade_tamanho = int(floor(tamanho/2))
    nova_s = "#" + s[:metade_tamanho] + "#" + s[metade_tamanho:] + "#"
    return nova_s