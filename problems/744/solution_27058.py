# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    d=round(len(s)/2)
    return '#'+s[0:round(len(s)/2)-0.5]+"#"+s[round(len(s)/2)-1:len(s)]+"#"