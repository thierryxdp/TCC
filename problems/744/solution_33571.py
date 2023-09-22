# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma palavra e insere # no inicio, meio e final'''
 
     i=len(s)
     f=i//2
     
     return "#"+ s[:f]+"#"+ s[f+1:]+"#"