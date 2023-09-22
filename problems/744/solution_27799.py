# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    p1=s[0:len(s)//2]
    p2=s[len(s)//2:]
    lista=['',p1,p2,'']
    lista=str.join('#',lista)
    return lista