# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    half = len(s) // 2
    a = s[0:half]
    b = s[half:]
    return str('#') + a str('#') + b + str('#')