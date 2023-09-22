def hashtag(s):
    '''retorna a string com hashtag inclusa no inicio no meio e no fim'''
    '''string ---> string'''
    t = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return t