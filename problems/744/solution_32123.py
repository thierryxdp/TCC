# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Tem como objetivo inserir um # no início, no meio e no
    final de uma string.
    str > str"""
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #s = "#" + pre + "#" + pos + "#"
    s = "#" + s[:len(str1)//2] + "#" + s[len(str1)//2:] + "#"
    return s