def retira_pontuacao(frase):
    """ """
    novafrase=''
    for x in range(len(frase)):
        if frase[x] in '?./,-:;-':
            novafrase+=''
        else:
            novafrase+=frase[x]
    return novafrase

def inverte(frase):
    """ """
    fraseinvertida=' ' 
    frase1=retira_pontuacao(frase)
    frase2=str.lower(frase1)
    frase3=str.split(frase2,'')
    
    def frase4(h):
        """ """
        for x in range(len(h)):
            if x< len(h) and h[x]=='':
                del(h[x])
        return h