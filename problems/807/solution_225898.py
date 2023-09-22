def conta_frases(texto):
    '''dado um texto como entrada, retorna a quantidade de
    frases existentes nele;
    stri -> int'''
    quan_palavras=str.split(texto,'?')
    quan_palavras=str.join(',',quan_palavras)
    quan_palavras=str.split(quan_palavras,'...')
    quan_palavras=str.join(',',quan_palavras)
    quan_palavras=str.split(quan_palavras,'!')
    quan_palavras=str.join(',',quan_palavras)
    quan_palavras=str.split(quan_palavras,'.')
    quan_palavras=str.join(',',quan_palavras)
    quan_palavras=str.split(quan_palavras,',')
    if quan_palavras[-1]=='':
        del(quan_palavras[-1])
    return len(quan_palavras)