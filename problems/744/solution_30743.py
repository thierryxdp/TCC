# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    resultado = '#' + s[:len(s)//2] + s[len(s)/2:] + '#'
    return resultado