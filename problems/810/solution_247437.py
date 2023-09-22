def inverte(frase):
    ''' docs '''
    
    # Passo 1. coloca em caixa baixa
    frase = str.lower(frase)
    
    # Passo 2. remove pontuação da frase
    
    
    # Passo 3. Separa a frase em palavras
    frase_dividida = str.split(frase_sem_pontuacao, ' ')
    
    # Passo 4. Inverte a frase (sem pontuação)
    frase_invertida = frase_divida[::-1]
    
    return frase_invertida