def hashtag(s):
    '''funcao que insere uma hashtag (#) no inicio, meio e fim de uma string
    str s; str -> str'''
    import math
    x = (math.floor(len(s)/2))
    subs1 = s[0:]
    subs2 = [x:]
    return '#' + str (subs1) + '#' str (subs2) + '#'