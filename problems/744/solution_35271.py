# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2==0:
     return "#"+ s[0:len(s)/2]+s[len(s)/2:]+"#"
    else:
        return "#"+s[0:]+"#"