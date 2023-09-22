def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
   
    texto_semP=str.split(texto,'.')
    texto_semR=str.split(texto,'...')
    texto_semE=str.split(texto,'!')
    texto_semI=str.split(texto,'?')
    
    quant_frases=texto_semP+texto_semR+texto_semE+texto_semI
    
    return quant_frases