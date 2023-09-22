# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string s e insere um caractere '#' no inicio, no meio e no final dela'''
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'