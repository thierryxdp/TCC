# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe um str e coloca # entre ela;str->str'''
    x = s[:len(s)//2]
    y= s[len(s)//2:]
    s = "#" + x + "#" + y + "#"
    return s