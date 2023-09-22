def hashtag(s):
    '''funcao'''
    numerodeletras = len(s)
   	s1 = s
    meio_par = int(numerodeletras/2)
    meio_impar = int((numerodeletras//2)-1)
    s2 = "#"+s1[:meio_par]+"#"+s1[meio_par:]+"#"
    s3 = "#"+s1[:meio_impar]+"#"+s1[meio_impar:]
    if (numerodeletras//2) == 0:
        return s2
    else:
        return s3