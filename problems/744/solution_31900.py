# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """insere o caractere "#" no ínicio,no meio e no final da string"""
    """str-> str"""
    b = len(s)/2
    s2 = '#'+s[:b]+'#'+s[b:]+'#'
    return s2