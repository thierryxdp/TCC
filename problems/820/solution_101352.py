def posLetra(f,letra,i):
    "Retorne a posição de uma letra em uma string pela i vez; str,str,int->int"
    c=1
    ii=0
    if i>f.count(letra):
        return -1
    while letra in f:
        if f[ii]==letra:
            if c==i:
                return ii
            c+=1
            
        ii+=1
    
    return -1