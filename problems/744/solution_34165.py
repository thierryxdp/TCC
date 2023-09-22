def hashtag(s):
    '''dada string s retorna com # no início, meio e fim da mesma
    str->str'''
    a="#"+s[:(len(s)//2)]+"#"+s[(len(s)//2):]+"#"
    return a