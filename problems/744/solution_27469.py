# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que recebe uma string e insere o caractere # no inicio, meio e fim
da string"""
    metadeString = len(s)//2
    return '#' + s[:metadeString] + '#' + s[metadeString:] + '#'