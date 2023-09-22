# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string s dada como entrada e retorna essa string com o acréscimo de uma # no ínicio, meio e fim. str->str'''
    tam=len(s)
    x=tam//2
    a='#'
    return a+s[0:x]+a+[x:]+a