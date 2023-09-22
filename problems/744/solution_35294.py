# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=(len(s)/2)
    if len(s)%2==0:
        return "#"+ s[0:x]+"#"+s[x:]+"#"
    else:
        return "#"+s[0:]+"#"