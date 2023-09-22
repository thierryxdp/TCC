# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade = len(s)//2
    
    return '#' + s[:metade+1] + '#' + s[metade - 1:] + '#'