def conta_frases(texto):
    '''Dado um texto em string, conta quantas frases estão no texto
    str->int'''
    texto_semPonto=str.split(texto,'.')
    texto_sem3P=str.split(texto,'...')
    texto_semEx=str.split(texto,'!')
    texto_semIn=str.split(texto,'?')
    texto_final=texto_semPonto+texto_sem3P+texto_semEx+texto_semIn
    quant_frases= len(texto_final)
    return quant_frases