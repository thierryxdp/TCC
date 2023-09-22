def conta_frases(texto):
    '''funcao que retorna o numero de frases em um texto'''
    numpt=len(texto.split('.'))
    numint=len(texto.split('?'))
    numex=len(texto.split('!'))
    num3p=len(texto.split('...'))
    numrep=3*(list.count(texto,'...'))
    return (numpt-1-numrep)+(numint-1)+(numex-1)+(num3p-1)