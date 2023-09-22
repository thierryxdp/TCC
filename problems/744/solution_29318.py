# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere '#' no início da tring; str -> str'''
    j=(s/2)
    sub1=s[0:len(j)]
    sub2=s[len(j):]
    return str(sub1)+str(sub2)