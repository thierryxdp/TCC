# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade = len(s)
    
    return '#'s[:metade+1] + '#' + s[metade:] + '#'