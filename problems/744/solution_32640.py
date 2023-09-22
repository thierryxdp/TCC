# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que dada uma string insere o caractere # no início, no meio e no
        fim dela
        str -> str
    '''
    i = len(s)
    str_com_hashtag = "#" + str(s[0:int(i/2)]) + "#" + str(s[int(i/2):]) +"#"
    return str_com_hashtag