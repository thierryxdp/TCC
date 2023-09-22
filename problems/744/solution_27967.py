def hashtag(s):
    '''Função que recebe uma palavra e retorna com um caractere(#) no início,
    no meio e no final dela, dada s=palavra (entre aspas)
    str->str'''
    
    s1=(len(s))//2
    s2=s[:s1]
    s3=s[s1:]
    
    return ('#'+s2+'#'+s3+'#')