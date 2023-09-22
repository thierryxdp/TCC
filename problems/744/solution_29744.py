# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' retorna uma string com o caractere "#" no inicio, no meio e no final dela'''
    ''' str -> str'''
    
    metade_1 = s[:(s)/2]
    metade_2 = s[(s)/2]
    hashtag = str('#') + metade_1 + str('#') + metade_2 + str('#')
    
    return hashtag