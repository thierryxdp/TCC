def conta_frase(frase):
    '''conta quantas frases tem no periodo dado'''
    
    interrogaçao = str.count(frase,'?')
    ponto_final = str.count(frase, '.')
    reticiencias = str.count(frase, '...')
    exclamaçao = str.count(frase, '!')
    return (interrogaçao + ponto_final + reticiencias + exclamaçao)