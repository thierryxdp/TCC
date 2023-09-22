# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
'''recebe uma string s e retorna outra string com hashtags no inicio, meio e final da string original; str -> str'''
if int(len(s))%2==0:
    return '#' + s[:int(len(s))/2] + '#' + s[int(len(s))/2:] + '#'
else:
    return '#' + s[:(int(len(s))//2)] + '#' + s[int(len(s))//2:] + '#'