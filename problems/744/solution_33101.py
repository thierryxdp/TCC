# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)%2 == 0:
        return str(len(s)) + ' é par'
    else:
        return str(len(s)) + ' é impar'