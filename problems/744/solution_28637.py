# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i=len(s)//2
    a=s[0:i]
    b=s[i:]
    text='#'+a+'#'+b+'#'
    return text