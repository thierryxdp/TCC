# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2==0:
        return "#"+s[:len(s)/2+1]+"#"+s[len(s)/2:]+"#"
    else:
        return "#"+s[:len(s)//2+1]+"#"+s[len(s)//2:]+"#"