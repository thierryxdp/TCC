# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''inclui o # no ínicio, meio e final da palavra s'''
    final = len(s)
    half = len(s)//2
    resposta = '#' + s[0:half] + '#' + s[half:final] + '#'
    return resposta