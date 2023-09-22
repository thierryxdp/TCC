# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    d=round(len(s)/2)
    return '#'+str(s[0:d-0.5])+"#"+str(s[round(len(s)/2):len(s)])+"#"