def hashtag(s):
    '''função que rotorna uma string com # no inicio,meio e fim. str->str'''
    h1=len(s)//2
    h2=s[:h1]
    h3=s[h1:]
    return '#'+ h2 +'#'+ h3 +'#'