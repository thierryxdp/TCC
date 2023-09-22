def hashtag(s):
    '''funcao'''
    n = len(s)
    meio_par = int(n/2)
    meio_impar = int((n//2)-1)
    s2 = "#"+s[:(meio_par)+1]+"#"+s[(meio_par)+1:]+"#"
    s3 = "#"+s[:meio_impar]+"#"+s[meio_impar:]+"#"
    if (n//2) == 0:
        return s2
    else:
        return s3