def inverte(frase):
    frase=str.lower(frase)
   	
    frase_sem_pontuacao = frase.replace('-',' ').replace(',','').replace('.','').replace('!','').replace('?','')
    
    frase_dividida=str.split(frase_sem_pontuacao,' ')
    
    frase_invertida = frase_dividida[::-1]
    return str.join(' ',frase_invertida