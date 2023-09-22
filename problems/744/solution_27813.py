# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'Define a função que retorna a string t 2 hashtag no início, meio e fim de uma string'
    'str-> str'
    t = '#'
    tamanho = len(s)
    metade = len(s)//2 - 1
    if s == ' ':
        t = t + '##'
    elif s == 'a':
        t = 'a' + '##'
    else:
        for j in range(tamanho):
            t = t + s[j]
            if j == metade or j == tamanho-1:
                t = t + '#'
    return t