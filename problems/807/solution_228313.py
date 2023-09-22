def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
    texto_semPonto=str.split(texto,'.')
    texto_semInt=str.split(texto,'?')
    texto_semEx=str.split(texto,'!')
    texto_semRet=str.split(texto,'...')
    
    quant_semEx=len(texto_semEx)-1
    quant_semInt=len(texto_semInt)-1
    quant_semRet=len(texto_semRet)-1
    quant_semPonto= len(texto_semPonto)-1-(quant_semRet)*3
    
    quant_frases=(quant_semEx)+(quant_semInt)+(quant_semRet)+(quant_semPonto)
    
    return quant_frases