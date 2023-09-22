def uppCons(frase):
    '''Dado uma frase, a função deve retornar outra frase só
    que com todas as consoantes em maiúscula;
    str ->str'''
    
    consoante_minuscula=[a,e,i,o,u]
    i=0
    n= len(frase)
    
    while(i<n):
        if(frase[i] in consoante_minuscula):
            frase = frase + str.upper(frase[i])
        i=i+1
        
    return (frase)