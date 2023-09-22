def uppCons(frase):
    '''recebe uma frase como entrada e a retorna com todas
    as suas consoantes em maiúsculas.
    str -> str'''
    
    i=0
    
    while i<len(frase):
        if frase[i] not in 'AEIOUÁÉÍÓÚÃÕÊÔaeiouáéíóúãõêô':
            nova_frase = nova_frase + frase[i]
        elif frase[i] in 'AEIOUÁÉÍÓÚÃÕÊÔaeiouáéíóúãõêô':
            nova_frase = nova_frase + str.upper(frase[i])
    i = i+1       
    return nova_frase