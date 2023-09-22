# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que recebe uma string que insira o caractere # no inicio, no meio e no final dela"""
    a= len(s)
    b= a//2
    c= "#" + s[0:b] + "#" + s[b:] + "#"
    return str(c)