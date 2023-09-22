# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """insere o caractere "#" no ínicio,no meio e no final da string"""
    """str-> str"""
    i = len(s)
    s2 = '#'+s[:int(i/2)]+'#'+s[int(i/2):]+'#'
    return s2