# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''hashtag recebe uma string e devolve uma string com o caractere"#" no início, no meio e no final dela.
    str-->str'''
    total=(len(s))//2
    string1=s[ :total]
    string2=s[total: ]
    return '#'+string1+'#'+string2+'#'