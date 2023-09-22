def inverte(frase):
    '''inverte a ordem das palavras de uma frase'''
    #passo 1 colocar em caixa baixa
    frase=str.lower(frase)
    
    #passo 2 remover a pontuação
    frase_sem_pontuacao=frase.replace('-',' ').replace(',','').replace(':','').replace(';','').replace('?','').replace('!','').replace('.','')
    
    #passo 3 separar a frase em palavras
    frase_dividida=str.split(frase_sem_pontuacao,' ')
    
    #passo 4 inverter a frase
    frase_invertida=frase_dividida[::-1]
    
    return str.join(' ', frase_invertida)