# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    """função que dada uma string, isere um # no inicio, meio e fim da string
    string=>string"""
    meio=int(len(string)/2)
    return '#' + string[:meio] + '#' + string[meio:] + '#'