# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que dada uma string, isere um # no inicio, meio e fim da string
    str=>str"""
    meio=int(len(string)/2)
    return '#' + string[:meio] + '#' + string[meio:] + '#'