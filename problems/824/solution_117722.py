def uppCons (frase):
    ''' função que retorna a frase só que com todas as consoantes em maiúsculas
    str->str'''
    
    i= 0 
    
    while i < len(frase):
        if frase [i] in 'qwszdxrcftgvyhbjnkmlpç':
            str.replace (frase,frase[i],(str.upper(frase[i])))
        i=i+1
    return frase