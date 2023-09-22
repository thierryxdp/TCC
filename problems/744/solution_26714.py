def hashtag(string):
    '''Recebe uma string e adiciona um '#' no começo, no meio e no fim da string
    str -> str'''
    return "#" + string[:(len(string)//2)] + "#" + string[(len(string)//2):] + "#"