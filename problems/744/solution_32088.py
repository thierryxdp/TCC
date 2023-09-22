# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string=s
   x=len(s)
    return "#" + s[:x/2] + "#" + s[x//2:]+"#"