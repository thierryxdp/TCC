# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade = int(len(s)/2)
    Resultado = str('#') + s[0:metade] + str('#') + s[metade:len(s)]