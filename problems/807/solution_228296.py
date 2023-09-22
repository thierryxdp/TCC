def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
   
    texto_semR=str.strip(texto,'...')
    texto_semE=str.strip(texto_semR,'!')
    texto_semI=str.strip(texto_semE,'?')
    texto_semP=str.strip(texto_semI,'.')
    
    quant_frases=len(texto_semP+texto_semR+texto_semE+texto_semI)-4
    
    return quant_frases