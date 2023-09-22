# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna s com # no iício meio e fim, str-> str"""
    a= len(s)//2
    return str('#')+s[0:a]+str('#')+s[a:]+str('#')