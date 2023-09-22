def uppCons(frase):
    '''recebe uma frase como entrada e a retorna com todas
    as suas consoantes em maiúsculas.
    str -> str'''
    
    i=0
    
    while i<len(frase):
        if frase[i] in 'AEIOUÁÉÍÓÚÃÕÊÔaeiouáéíóúãõêô':
            return frase
        elif frase[i] not in 'AEIOUÁÉÍÓÚÃÕÊÔaeiouáéíóúãõêô':
            nova_frase = nova_frase + str.upper(frase[i])
            
    return nova_frase