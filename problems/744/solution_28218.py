# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''coloca um caracter no comeco, no meioe no fim da str'''
    i=len(s)//2
    return '#' + s[:i] + '#' + s[i:] + '#'