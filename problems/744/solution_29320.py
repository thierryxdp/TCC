# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere '#' no início da tring; str -> str'''
    j=(len(s)/2)
    sub1=s[1:j]
    sub2=s[j:]
    return str(sub1)+str(sub2)