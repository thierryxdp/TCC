# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Reorna uma string com uma hastag no inicio, centro e fim;
    str --> str"""
    centro = len(s) // 2
    buffer = '#' + s[:centro] + '#' + s[centro:] + '#'
        
    return buffer