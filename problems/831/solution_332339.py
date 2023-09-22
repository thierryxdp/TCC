def lingua_p(palavra):
    '''
    exemplo-> epexepemplopo
    '''
    x=str.lower(palavra)
    i=0
    palavraP=''
    while i<len(x)
        if x[i] in "aeiou":
            palavraP=palavraP+x[i]+"p"+x[i:]
        i=i+1
    return palavraP