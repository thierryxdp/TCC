# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2==0:
        p=len(s)//2
    else:
        p=(len(s)-1)//2
        
        
        return '#'+s[:p]+'#'+s[p:]+'#'