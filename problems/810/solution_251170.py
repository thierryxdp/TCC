def retira_pontuacao(frase):
    """..."""
    novafrase=''
    for x in range(len(frase)):
        if frase[x] in "?.!,—:;-":
            novafrase+=' '
        else:
            novafrase+=frase[x]
    
    return novafrase
    
def inverte(frase):
    """..."""
    fraseinvertida=''
    frase1=retira_pontuacao(frase)
    frase2=str.lower(frase1)
    frase3=str.split(frase2,' ')
    for x in range(len(frase3)):
        x+=1
        fraseinvertida+=frase3[-x]
        
    return fraseinvertida