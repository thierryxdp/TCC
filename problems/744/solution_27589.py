# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que ao receber uma string se insere o caractere'#' no inicio,
     no meio e no final dela. str->str'''
    len(s)
    a=s[0:((len(s))//2)]
    b=s[((len(s))//2):]
    return str("#"+a+"#"+b+"#")