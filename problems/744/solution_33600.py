# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    if len(s)%2==0:
        new='#'+s[0:int((len(s)/2))]+'#'+s[int((len(s)/2)+1):]+'#'
        return new
    else:
        new='#'+s[0:int((len(s)/2))]+'#'+s[int((len(s)/2)+2):]+'#'
        return new