# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' retorna uma concatenação de strings com # a partir de uma dada string s e com #'s no incio meio e fim
    str->str'''
    return str("#") + str(s[0:len(s)//2]) + str("#") + str(s[len(s)//2:]) + str("#")