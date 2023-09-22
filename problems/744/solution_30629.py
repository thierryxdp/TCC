# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que retorna uma # antes, no meio e 
    depois de uma cadeia de caracteres de uma string
    string=>string"""
    primeira_parte = len(s)//2

    string_saida = '#' + s[0:primeira_parte] + '#' + s[primeira_parte: len(s)] + '#'
    return string_saida