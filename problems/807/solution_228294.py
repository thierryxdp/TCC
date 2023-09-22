def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
   
    texto_semP=str.split(texto,'.')
    texto_semR=str.split(texto_semP,'...')
    texto_semE=str.split(texto_semR,'!')
    texto_semI=str.split(texto_semE,'?')
    
    quant_frases=texto_semP+texto_semR+texto_semE+texto_semI
    
    return quant_frases