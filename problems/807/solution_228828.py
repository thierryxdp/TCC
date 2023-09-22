def conta_frases (frase):
    '''
    	Recebe uma frase e conta qunatas frases estão contidas nela.
        Parâmetro 1: string
        Resultado: int
    '''
    nova_frase = str.replace(str.replace(str.replace(str.replace(frase, '...', '*'), '?', '*'), '!', '*'), '.', '*')
    frases = str.split(nova_frase, '*')
    frase.remove('')
    return len(frases)