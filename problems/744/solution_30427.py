# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """"""
    if len(s)%2 == 0:
        fatiamento_par = len(s)/2
        stringfinal= '#' +str(s[0:len(s)]) 
        + '#' +str(s[len(s)/2:])+ '#'
        return stringfinal