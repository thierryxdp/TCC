# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """a função
    Entrada: string
    Saída: string"""
    s1 = '#' + s[0:2]
    s2 = '#' + s[2:5]
    s3 = s[6:] + '#'
     return s1 + s2 + s3