def conta_frases(texto):
    '''funcao que retorna o numero de frases em um texto'''
    numpt=len(texto.split('.'))
    numint=len(texto.split('?'))
    numex=len(texto.split('!'))
    num3p=len(texto.split('...'))
    if '...'in texto:
        return (numpt-4)+(numint-1)+(numex-1)+(num3p-1)
    else:
        return (numpt-1)+(numint-1)+(numex-1)+(num3p-1)