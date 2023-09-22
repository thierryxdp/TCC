def hashtag(s):
    '''funcao'''
    def hashtag(s):
    '''funcao'''
    n = len(s)
    meio = n//2
    s2 = "#"+s[:meio ]+"#"+s[meio :]+"#"
    s3 = "#"+s[:meio +1]+"#"+s[meio+1:]+"#"
    if (n//2) == 0:
        return s2
    else:
        return s3