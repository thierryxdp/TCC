# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que receba uma string e insira o caractere "#" no inicio, no meio e no final
    str -> str'''
    x=len(s)
    z=x//2
    return '#'+s[0:z]+'#'+s[z:]+'#'