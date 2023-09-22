def conta_frases(texto):
    '''funcao que retorna o numero de frases em um texto'''
    numpt=(texto.split('.'))
    numint=(numpt.split('?'))
    numex=(numint.split('!'))
    num3p=(numex.split('...'))
    return len(num3p)