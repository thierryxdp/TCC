# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada ums string retorna com caractere # no início, meio e fim da string
    str -> str'''
    
    i = len(s)//2
    sub = s[0:i]
    
    return '#' + sub + '#' + s[i:] + '#'