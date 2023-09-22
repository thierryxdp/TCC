# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    """devolve uma string com # no inicio, meio e fim
    string->string
    """
    return "#"+string[0:(len(string)+1)]+"#"+string[(len(string)+1):]