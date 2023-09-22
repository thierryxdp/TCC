# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)
    y=int(x)//2
    resposta="#"+s[0:y]+"#"+s[y:]+"#"
    return resposta