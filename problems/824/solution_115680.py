def uppCons(frase):
    i=0
    resposta=''
    while i<len(frase):
        if frase[i] in 'qwrtypçlkjhgfdszxcvbnmQWRTYPÇLKJHGFDSZXCVBNM':
            resposta+=str.upper(frase[i])
        else:
            resposta+=frase[i]
    	i=i+1
    return resposta