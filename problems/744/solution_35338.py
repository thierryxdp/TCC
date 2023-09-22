# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que recebe e insere o caractere '#' no inicio, no meio e no final'''
return '#' + s[:(len(s)//2] + '#' + s[(len(s)//2:] + '#'