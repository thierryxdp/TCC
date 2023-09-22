# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    num=len(s)//2
    num1=num-1
    num2=num+1
    return '#'+s[0:num1]+'#'+s[num2:]+'#'