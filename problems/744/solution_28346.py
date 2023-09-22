# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ recebe str e retorna tupla"""
    s="#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    return s