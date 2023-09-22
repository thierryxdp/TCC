def conta_frases(frase):
    '''Função que dado um texto conta quantas frases que aparecem dele, essa frases devem terminar com o ponto final, ponto de exclamação, ponto de interrogação ou reticências
     String->string''' 

    
    frase= str.replace(frase,'...','.')
    frase=str.replace(frase,'.','.')
    frase= str.replace(frase,'?','.')
    frase=str.replace(frase,'!','.')
    frase_final=str.count(frase,'.')
    
    return frase_final