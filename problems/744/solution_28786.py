# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que coloca # no inicio, no meio e 
    no final da string'''
    s= '#' +s[:len(s)//2]+ '#' +s[len(s)//2:]+ '#'
        return s