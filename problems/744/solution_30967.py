# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna uma str com # nos início, meio e fim
    str -> str'''
    return str('#')+str(s)[0:len(s)//2]+str('#')+str(s)[len(s)//2:]+str('#')