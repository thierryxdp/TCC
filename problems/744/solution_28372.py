# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Receba uma string s e coloca o caractere ”#” no início, no meio e no final dela"""
    """ str -> str """
    return "#" + str(s)[0:(len(str(s))//2)] + "#" + str(s)[(len(str(s))//2):len(str(s))] + "#"