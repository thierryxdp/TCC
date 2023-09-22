def conta_frases(texto):
    '''Dado um texto em string, retorna uma função que diz quantas frases tem no texto
    str->int'''
    texto_semRet=len(str.split(texto,'...'))-1
    texto_semEx=len(str.split(texto,'!'))-1
    texto_semInt=len(str.split(texto,'?'))-1
    texto_semPonto=len(str.split(texto,'.'))-1
    quant_frases= (texto_semPonto+texto_semRet+texto_semEx+texto_semInt)//4
    
    return quant_frases