# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''inserçao de um caracter especial no inicio, no meio e no fim da palavra;
    str -> str'''
    hashtag = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return hashtag