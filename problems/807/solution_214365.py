def conta_frases(texto):
    ''' essa funcao retorna a quantidade de frases em um texto dado de entrada '''
    
    textosubs = texto.replace('!','#').replace('?','#').replace('...','#').replace('.','#')
    contar = textosubs.count('#')
    
    return contar