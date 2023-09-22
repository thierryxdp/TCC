# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    tag ='#'
    contador=len(s)//2
    return tag+s[0:contador]+tag+s[contador:]+tag