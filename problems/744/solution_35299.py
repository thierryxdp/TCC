# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    centro = len(s) // 2
    buffer = '#' + s[:centro] + '#' + s[centro:] + '#'
        
    return buffer