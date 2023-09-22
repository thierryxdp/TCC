def uppCons(frase):
    '''recebe uma frase e retorna a frase com todas as consoantes em 
    maiúscula.
    str ->str'''
    nova =''
    i =0
    while i <len(frase):
        if frase[i] not in 'aeiouáéíóúÁÉÍÓÚAEIOU':
            nova = nova +str.upper(frase[i])
    
        else:
            nova =nova +frase[i]
        i =i+1
    return nova