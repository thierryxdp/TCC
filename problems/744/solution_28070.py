# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna um string com uma hashtag no início, no meio e no final dela
    str->str'''
    
    metade = len(s)//2
    
    tags = str('#') + s[0:metade] + str('#') + s[-metade:] + str('#')
    
    return tags