# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    cont = int(len (s)/2)
    str1 = s
    str2 = '#' + str1[0: cont] + '#' + str1[cont:] + '#'

    return str2