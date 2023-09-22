def hashtag(s):
    '''Esta função retorna uma string com um caractere "#"
    no inicio, meio e final dela
    str-> str'''
    
    x = len(s)
    
    return '#' + s[0:x//2]+ '#' + s[x//2:] + '#'