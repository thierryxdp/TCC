def conta_frases(frase):

    '''Conta o número de palavras em uma frase '''

    # str -> int

    palavras = frase.count('.') + frase.count('!') + frase.count('?')
    palavras = palavras
    
    for dado in frase[0:]:
        
        if dado == '...':
            
            palavras = palavras - 2
    return palavras