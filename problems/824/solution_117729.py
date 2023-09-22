def uppCons (frase):
    ''' função que retorna a frase só que com todas as consoantes em maiúsculas
    str->str'''
    
    i= 0 
    palavras = ''
    
    while i < len(frase):
        if frase [i] in 'qwszdxrcftgvyhbjnkmlpç':
            palavras = palavras +(str.replace (frase,frase[i],(str.upper(frase[i]))))
        i=i+1
    return palavras