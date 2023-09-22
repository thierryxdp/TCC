# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''coloca hashtag no inicio, meio e fim de uma palavra recebida
       str -> str'''
    P=len(s)//2
    return str('#')+str(s[0:P])+str('#')+str(s[P:])+str('#')