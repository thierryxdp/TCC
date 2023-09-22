def uppCons (frase1):
    '''função que recebe uma frase de entrada (frase1) e que retorna
    todas as suas consoantes em maísuculo e as suas vogais iguais ao
    de entrada;
    str->str'''
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    c_todas = str.upper(consoantes)+ consoantes
    frase = frase1[i]+''
    while i<len(frase1):
        if frase1[i] in c_todas:
            c_nova = str.upper(frase1[i])
            frase = frase[:i] +  c_nova + frase1[(i+1):]
        i = i+1
    return frase