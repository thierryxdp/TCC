# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string e insere o caractere # no início, 
    no meio e no final dela
    str -> str"""
    z=len(s)
    r=z//2
    sub='#'+s[0:r]+'#'+s[r:]+'#'
    return sub