# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metadeString = len(s)//2
    return '#' + s[:metadeString] + '#' + s[metadeString:] + '#'