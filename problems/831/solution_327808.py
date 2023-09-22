def lingua_p(palavra):
    palavra_nova = str()
    
    for letra in palavra:
        if letra in 'aeiouéúáàíó':
            palavra_nova+= 'p'+str(letra)+'p'
    
    return palavra_nova