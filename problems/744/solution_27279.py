# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    tam = len(s)
    tam //= 2
    tag = '#'
    
    texto = tag + s[:tam] + tag + s[tam:] + tag
    return texto