def hashtag(string):
    '''
    funcao que recebe uma string
    e retorna ela mesma com o
    caractere # no inicio, um no
    meio e um no fim
    str->str
    '''
    m=len(string)//2
    return '#' + string[0:m] +'#'+string[m:]+'#'