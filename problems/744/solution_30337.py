# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string qualquer e retorna
    uma nova string com (#) no inicio, meio e fim da 
    string'''
    j = int (len(s)/2)
    subA = s [0:j]
    subB = s [j:]
    return '#' + subA + '#' + subB + '#'