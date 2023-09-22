# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma str e insira # no meio str>str"""
    return '#' + s[(len(s)//2)] + '#' + s[(len(s)//2):] + '#'