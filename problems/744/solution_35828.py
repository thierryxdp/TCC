def hashtag(s):
    '''funcao'''
    numerodeletras = len(s)
    meio_par = int(numerodeletras/2)
    meio_impar = int((numerodeletras//2)-1)
    s2 = "#"+s[:meio_par]+"#"+s[meio_par:]+"#"
    s3 = "#"+s[:meio_impar]+"#"+s[meio_impar:]+"#"
    if (numerodeletras//2) == 0:
        return s2
    else:
        return s3