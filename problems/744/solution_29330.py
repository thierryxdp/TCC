# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)==2,4,6,8,0:
        return str('#'+s[0:len(s)/2]+'#'+s[len(s)+1:30]+'#')
    else:
        if len(s)==1,3,5,7,9:
            return str('#'+s[0:len(s)/2-0.5]+'#'+s[len(s):30]+'#')