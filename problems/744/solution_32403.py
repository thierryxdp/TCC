def hashtag(s):
    ''' Retorna uma string com # no início, no meio 
    e no final dela '''
    # [:len(s)//2] + "#" + [len(s)//2:]
        return "#" + s[:len//2] + "#" + [len//2:] + "#"