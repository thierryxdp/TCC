def uppCons(frase  
    tot=len(frase)
    frase2=''
    cont=0
    while cont < tot:
        if frase[cont] in 'qwrtypçlkjhgfdszxcvbnm':
            frase2=frase2+str.upper(frase[cont])
        else:
            frase2=frase2+frase[cont]
        cont=cont+1
    return frase2