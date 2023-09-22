# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = len(s)//2
    s_part = s[0:l]
    
    return '#'+str.join('#', [s_part, s[l:len(s)])+'#'