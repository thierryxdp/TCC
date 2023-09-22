def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
    texto_semPonto=len(str.split(texto,'.'))
   
    quant_frases= texto_semPonto
    
    return quant_frases