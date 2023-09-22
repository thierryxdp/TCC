def hashtag(s):
    """ retorna uma str com o caractere '#'
    no inicio, no meio e no fim dela dado 
    uma str s.
    str -> str"""
    tamanho_de_s = len(s)
    metade = int(tamanho_de_s / 2)
    inicio_de_s = s[:metade]
    final_de_s = s[metade:]
    return "#" + inicio_de_s + "#" + final_de_s + "#"