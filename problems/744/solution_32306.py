# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' funcao que calcula onde colocar a # no meio da string  usa-se o len paea contar quantos algoritiomos
    e dividor por 2 para achar a metade;s= string'''
    meio1=s[len(s)//2: ]
     meio2=s[ :len(s)//2]
 return'#'+meio2+'#'+ meio1+'#'