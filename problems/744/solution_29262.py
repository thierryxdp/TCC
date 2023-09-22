# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere '#' no início da tring; str -> str'''
    sub1=s[0:len(s)/2]
    sub2=[len(s)/2:]
    return str('#'+sub1+'#'sub2+'#')