# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e adiciona no inicio, meio e funal eum #
    parametros str->str"""
    s = '#' + s[:len(s) // 2] + '#' + s[len(s) // 2:] + '#'
    return s