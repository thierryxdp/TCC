# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que retorna uma # antes, no meio e no final de uma string,
    seja de número de caracteres par ou ímpar"""
    primeira_parte = len(s)//2

    string_saida = '#' + s[0:primeira_parte] + '#' 
    + s[primeira_parte: len(s)] + '#'
    return string_saida