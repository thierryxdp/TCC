def conta_frases(texto):
    '''Dado um texto em string, conta quantas frases estão no texto
    str->int'''
    
    texto_final= str.split(texto,('...',',','!','?'))
    quant_frases= len(texto_final)
    
    return quant_frases