# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """a função
    Entrada: string
    Saída: string"""
    s1 = len(s)/2
    s2 = '#' + [:s1]
    s3 = '#' + [s1:] + '#'
     return s2 + s3