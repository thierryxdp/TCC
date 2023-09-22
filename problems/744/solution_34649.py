def hashtag(s):
    '''calcula string que insira # no início , meio e final
    str->str'''
    
    s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    
    return s