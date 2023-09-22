# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' funcao que insere caractere "#" no inicio, meio e final da mesma '''
    ''' str -> str '''
    x = '#'
    return x[0:s] + x[2:s] + s[:x]