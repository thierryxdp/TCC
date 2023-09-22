# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

def hashtag(s):
    if len(s)%2==0:
        return '#'+str(s[:int(len(s)/2)])+'#'+str(s[int(len(s)/2):])+'#'
    if len(s)%2!=0:
        return '#'+str(s[:int(len(s)/2-0.5)])+'#'+str(s[int(len(s)/2-0.5):])+'#'