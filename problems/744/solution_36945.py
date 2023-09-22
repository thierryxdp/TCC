def hashtag(s):
    '''troca a letra por #'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:]
    return s