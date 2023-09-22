# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a= len (s)/2
    b= len (s)%2
    c= floor (a)
    if (b==0):
        return '#' + s[0:c] + s[c:] + '#'
    elif (b==1):
        return '#' + s[0:c] + '#' + s[c:] + '#'