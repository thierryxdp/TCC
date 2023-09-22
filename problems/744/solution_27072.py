def hashtag(s):
    '''Calcula e retorna, a partir de uma string s, a inclusao de hashtag em diferentes posiçoes
    str -> str
    parameters:
    s: string qualuquer'''
    elemento_meio = len(s) // 2
    
    return '#' + s[0:elemento_meio] + '#' + s[elemento_meio:] + '#'