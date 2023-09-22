def hashtag(s):
    """ função que insere # no começo, meio
    e final da string
    string -> string"""
    x= (len(s)//2)
    return "#"+ s[0:x]+"#"+s[x:]+"#"