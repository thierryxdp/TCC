def conta_frases(texto):
    '''funcao que retorna o numero de frases em um texto'''
    numpt=len(texto.split('.'))
    numint=len(texto.split('?'))
    numex=len(texto.split('!'))
    num3p=len(texto.split('...'))
    return (numpt-1-3*(list.count(texto,'...'))+(numint-1)+(numex-1)+(num3p-1)