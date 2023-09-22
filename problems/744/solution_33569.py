# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma palavra e insere # no inicio, meio e final'''
    i=s.len%2
    return "#"+ s[:i]+"#"+ s[i+1:]+"#"