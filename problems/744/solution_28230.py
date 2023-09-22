# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Adiciona um hashtag no inicio, meio e fim da string
    str->str'''
    tamanho = len(s)
    return '#'+s[:tamanho//2]+'#'+s[tamanho//2:]+'#'