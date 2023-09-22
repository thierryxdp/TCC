def lingua_p (palavra):
    '''dada uma palavra, retorna essa palavra com o caracter p
    depois de cada vogal mais essa vogal'''
    
    palavra_p = ''
    
    for letra in palavra:
        if letra in 'AEIOUÁÉÍÓÚaeiouáéíóú':
            palavra_p += letra + 'p'+ letra
        else:
            palavra_p += letra
    return str.lower(palavra_p)