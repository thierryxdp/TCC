# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
     return ("#" + s [ 0:(round(len(s)/2))] + "#" + s[(floor(len(s)/2)):] + "#")