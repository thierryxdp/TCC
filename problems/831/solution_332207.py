def lingua_p(palavra):
    '''
    
    '''
    palavra = list(palavra.lower())
    i = 0 
    for letra in palavra:
        if letra in 'aeiou':
            insere = 'p' + x
            palavra.insert(palavra.index(letra,i)+1, insere)
        i += 1
        x = ''.join(palavra)
        return x