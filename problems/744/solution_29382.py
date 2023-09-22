# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funçao que divide a frase de entrada S por 3 hashtag's,uma no início,no meio e no final''' 
    '''str->str'''
    n=len(s)
    return '#'+s[0:n//2]+'#'+s[n//2:30]+'#'