def posLetra(frase, letra, n):
    qnt_letras = str.count(frase, letra)
    
    if qnt_letras < n:
        return -1
    else: 
        i=0
        p=0
        while i<len(frase):
            if frase[i]==letra:
                p= i
                            
            i+=1        
        return frase[i]