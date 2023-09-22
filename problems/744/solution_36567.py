# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = int(len(s))
    s1 = int(l//2)
    
    s1 = s[0:s1]
    #s2 = s[s1:l]
    return str.join('#', [s1])