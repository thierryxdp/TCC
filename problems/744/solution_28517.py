# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    pre = str1[:len(s)//2]
    pos = str1[len(s)//2:]
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s