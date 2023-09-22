# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere o caractere '#' no ínicio, no meio e no final de uma string s;
    str -> str'''
    meio_string = len(s)/2
    nova_string = '#' + s[0:meio_string] + '#' + s[meio_string + 1:]
    return nova_string