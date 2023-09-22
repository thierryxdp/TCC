def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'QWRTYPLKJHGFDSZXCVBNMqwrtyplkjhgfdszxcvbnmçÇ':
            frase=str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase