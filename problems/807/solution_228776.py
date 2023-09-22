def conta_frases(frase):

    '''Conta o número de palavras em uma frase '''

    # str -> int

    palavras = frase.count('.') + frase.count('!') + frase.count('?')
    palavras = palavras + 1
    
    for dado in frase:
        
        if dado == '...':
            
            palavras = palavras - 2
    return palavras