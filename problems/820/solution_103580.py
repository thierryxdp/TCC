def posLetra(frase, letra, n):
    qnt_letras = str.count(frase, letra)
    
    if qnt_letras < n:
        return -1
    
        i=0
        p=0
        while 1<len(frase):
            if frase[1]==letra:
                p+=1
            if p==n:
                return i
             1+=i