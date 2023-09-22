# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''dsd'''
    total_letras= len(s)
    if total_letras%2==0:
        metade_palavra =total_letras/2
        hashtag_meio= s[0:metade_palavra]
        return hashtag_meio