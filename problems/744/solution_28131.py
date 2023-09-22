# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Concatena # ao início, meio e fim da string;
    str->str"""
    returns str('#')+s[:(len(s)//2)]+str('#')+s[(len(s)//2):]+str('#')