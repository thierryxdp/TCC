def posLetra(frase, letra, n):
    qnt_letras = str.count(frase, letra)
    
    if qnt_letras < n:
        return -1
    
        i=0
        c=0
        while 1<len(frase):
            if frase[1]==letra:
                c+=1
            if c==n:
                return i
            i+=1
            return p