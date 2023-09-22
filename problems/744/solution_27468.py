# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que dada uma string s, retorna essa string com uma hashtag
       no começo, uma ne metade da string e outra na final. str -> str'''
    s_str = s
    has = s_str[:len(s)//2]
    htag = s_str[len(s)//2:]
    h = '#'
    return h + has + h + htag + h