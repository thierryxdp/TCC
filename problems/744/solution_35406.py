# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    L= len(s)
    M1=s[0:L//2]
    M2=s[L//2:]
   
    return '#'+ M1 +'#'+ M2 +'#'