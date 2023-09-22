def hashtag(s):
    '''calcula e retorna a string com # no início, meio e final; str->str'''
    c='#'
    d=len(s)//2
    return c+s[0:d]+c+s[d+1:]+c