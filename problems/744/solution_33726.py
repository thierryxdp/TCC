# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string e retorna essa mesma string com uma '#' no inicio, 
    no meio e no fim dela
    str-> str'''
    return '#'+ s[:len(s)//2]+'#'+s[len(s)//2:]+'#'