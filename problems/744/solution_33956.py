# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que retorna uma string com uma hashtag no início, no meio e no final'''
    return '#' + s[:(len(s)/2)+1] + '#' + s[len(s)/2:] + '#'