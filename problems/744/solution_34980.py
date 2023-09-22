# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s=list(s)
    s[0]='#'+s[0]
    s[(len(s)//2)]='#' +  s[(len(s)//2)] 
    s[len(s)-1) =  s[len(s)-1]+'#'
    return ''.join(s)