def hashtag(s):
    '''Recebe um sring s e retorna uma sting com "#"
    no começo, no fim e no meio para menos
    	str -> str'''
    n = len(s)//2
    h = '#'
    return h + s[:n] + h + s[n:] + h