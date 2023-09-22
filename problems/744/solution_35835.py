def hashtag(s):
    '''funcao'''
    n = len(s)
    meio_par =(n//2)+1
    meio_impar = (n//2)+1
    s2 = "#"+s[:meio_par]+"#"+s[meio_par:]+"#"
    s3 = "#"+s[:(meio_impar)]+"#"+s[(meio_impar)-1:]+"#"
    if (n//2) == 0:
        return s2
    elif n == 1:
        return"##"+s+"#"
    else:
        return s3