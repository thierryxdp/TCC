# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ função que insere o caracter "#" no inicio
    meio e fim da string fornecida.
    assinatura: str --> str
    """
    return '#'+ s[0:2]+'#'+s[3:len(s)]+'#'