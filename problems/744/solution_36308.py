# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    # dada uma string, retorna com caractere # no inicio, meio e f str-> str
    i= len (s)//2
    return '#' + s[:i] + '#' +s[i:] + '#'