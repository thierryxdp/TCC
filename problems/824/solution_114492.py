def uppCons(frase):
    ''' funcao recebe uma frase e retorna a mesma
    frase so que com sua consoantes maiuscula, str-->str'''
    i=0 
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxywz':
            str.upper(frase[1])
    i=i+1    
    return frase