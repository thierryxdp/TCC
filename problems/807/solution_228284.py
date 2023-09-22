def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
    texto_semPonto=len(str.split(texto,'.'))
    texto_semRet=len(str.split(texto,'...'))
    texto_semEx=len(str.split(texto,'!'))
    texto_semInt=len(str.split(texto,'?'))
    quant_frases= texto_semPonto+texto_semRet+texto_semEx+texto_semInt
    
    return quant_frases