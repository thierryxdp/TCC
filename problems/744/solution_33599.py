# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    if len(s)%2==0:
        new='#'+a[0:int((len(a)/2))]+'#'+a[int((len(a)/2)+1):]+'#'
        return new
    else:
        new='#'+a[0:int((len(a)/2))]+'#'+a[int((len(a)/2)+2):]+'#'
        return new