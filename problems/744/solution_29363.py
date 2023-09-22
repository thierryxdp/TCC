# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)>6:
        return str('#'+s[0:2]+'#'+s[len(s)+3:30]+'#')
    else:
        if len(s)<6:
            return str('#'+s[0:3]+'#'+s[4:30]+'#')