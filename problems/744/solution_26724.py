# Hashtag.
# str-> str
def hashtag(s):
    '''Essa função deverá inserir uma hashtag no inicio, no meio e no final da frase inserida;
    STR -> STR'''
    return '#' + s[:len(s)//2]+'#'+s[len(s)//2:]+'#'