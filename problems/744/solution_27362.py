# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'Funcao que recebe uma string e insere o caractere # no inicio, no meio e no final dela'
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'