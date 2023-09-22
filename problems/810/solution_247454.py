def inverte(frase):
    ''' docs '''
    
    # Passo 1. coloca em caixa baixa
    frase = str.lower(frase)
    
    # Passo 2. remover pontuação da frase
    retira_pontuacao = frase.replace('!','').replace('-',' ').replace('?','').replace('.','').replace(',','').replace(':','').replace(';','')
        return frase
    
    # Passo 3. separa a frase em palavras
    frase_dividida=str.split(retira_pontuacao, ' ')
    
    # Passo 4. inverte a frase (sem pontuação)
    frase_inverte = frase_dividida[::-1]
    
    return str.join(' ', frase_invertida)