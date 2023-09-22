# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string e adiciona '#' no começo, meio e fim desta
    str->str"""
    meio = len(s)//2
    return '#' + s[0:meio] + '#' + s[meio:] + '#'