# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que receba uma string'#' no inicio, meio e final dela'''
    ''' str-> str '''
    s="#"+s[(s)//2]+"#"+s[(s)//2]+"#"
    return s