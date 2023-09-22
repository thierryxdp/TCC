# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """concatena hastags no início, meio e fim das strings;string->string"""
    if len(s)==10:
        return '#'+ s[:5]+ '#' + s[5:]+'#'