# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere o caracter '#' no incio, no meio e no final de uma dada string
    str -> str'''
    meio_str = len(s) // 2
    return '#' + s[:meio_str] + '#' + s[meio_str:] + '#'