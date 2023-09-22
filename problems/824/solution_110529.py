def uppCons(frase):
    '''Recebe uma frase a analisa o parâmetro de entrada e retorna todas 
    as consoantes encontradas em maiúsculas e os demais caractéres no formato original
    tupla -> tupla'''
    
    consoantes = ('b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z')
    i = 0
    
    while i < len(frase):
        if frase[i] in consoantes:
            str.replace(frase, frase[i] ,frase[i].upper())
        i = i + 1
    return frase