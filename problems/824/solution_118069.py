def uppCons (frase):
    '''Esta função retorna uma frase com todas as suas consoantes 
    em maiusculas.
    str >>> str '''
    i = 0
    maiusculas = ''
    frase_maiuscula = ''
    
    while i < len(frase): 
        maiusculas = frase[1]
        if frase[1] in 'qwrtypsdfghjklçzxcvbnm':
            maiusculas = str.upper (maiusculas)
        frase_maiuscula = frase_maiuscula + maiusculas
        i = i + 1
    return frase_maiuscula