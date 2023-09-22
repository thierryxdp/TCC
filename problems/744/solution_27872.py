# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''recebe uma string e insere # no começo, meio e fim da string.'''
    tamanho = len(s)
    return '#' + s[:tamanho//2] + '#' + s[tamanho//2:] + '#'