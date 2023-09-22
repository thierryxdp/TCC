# Função insere '#' em um dado texto s no início, na metade e no final
# s: texto qualquer, metade: metade de s, h = '#'
# str-> str
def hashtag(s):
    metade = int(len(s)/2)
    h = '#'
    return h + s[:metade] + h + s[metade:] + h