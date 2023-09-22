# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que receba uma string e insira o caractere '#' no inicio,meio e no final dela; str-> str"""
    s= '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'
    return s