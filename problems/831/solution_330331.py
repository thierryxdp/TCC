def lingua_p(palavra):
    '''
        Funcao recebe uma palavra em portugues e retorna
        essa palavra traduzida para a lingua do P.
        str -> str
        
    '''
    palavra = palavra.lower()
    palavra = list(palavra)
    copia_palavra = list.copy(palavra)
    
    for letra in copia_palavra:
        if letra in 'aeiou':
            palavra.insert((palavra.index(letra) + 1),'p')
            palavra.insert((palavra.index(letra) + 2), letra)
        
    palavra = str.join('',palavra)
    return palavra