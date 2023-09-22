def conta_frases(frase):
    ''' Função que retorna o número de frases em um texto.
        str -> int
    '''
    frase = str.replace(frase,'...','/')
    frase = str.replace(frase,'.','/')
    frase = str.replace(frase,'!','/')
    frase = str.replace(frase,'?','/')
    return len(str.split(frase,'/')) -1