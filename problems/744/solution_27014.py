# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    abcd= int(s[0:3])
    abcde= int(s[0:4])
    has1= str(#)+s[0:1]+str(#)+s[2:3]
    has2= str(#)+s[0:1]+str(#)+s[2:4]
    if s==abcd:
        return has1
    elif s==abcde:
        return has2