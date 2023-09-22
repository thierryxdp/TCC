def hashtag(s):
    '''
    Função que recebe uma string e retorna a string dividida com três
    hashtags início, meio e fim
    '''
    caract_s = len(s)
    meio = caract_s//2
    meio1 = s[0:meio]
    meio2 = s[meio:caract_s]
    return '#' + meio1 + '#' + meio2 + '#'