def hashtag(s):
2
    ''' Retorna uma string com # no início, no meio 
3
    e no final dela '''
4
    # s[0:len(s)//2] + "#" + [len(s)//2:0]
5
        return "#" + s[0:len(s)//2] + "#" + s[len(s)//2:0] + "#"