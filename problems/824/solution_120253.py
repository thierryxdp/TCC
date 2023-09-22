def uppCons(frase):
    '''Dado uma frase, a função deve retornar outra frase só
    que com todas as consoantes em maiúscula;
    str ->str'''
    
    consoante_minuscula='qwrtypsdfghjklzxcvbnm'
    i=0
    n= len(frase)
    frase2= ''
    
    while(i<n):
        if(frase[i] in 'qwrtypsdfghjklzxcvbnm'):
            frase2 = frase2 + str.upper(frase[i])
        
        i=i+1
        
    return (frase)