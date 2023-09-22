def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
   
    texto_semP=str.strip(texto,'.')
    texto_semR=str.strip(texto_semP,'...')
    texto_semE=str.strip(texto_semR,'!')
    texto_semI=str.strip(texto_semE,'?')
  
    quant_frases=len(texto_semI)
    
    return quant_frases