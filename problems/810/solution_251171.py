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
    """Recebe uma frase e retorna essa frase sem pontuação, letras maiúsculas e com as palavras da frase em ordem inversa.
    Assinatura: str -> str"""
    fraseinvertida=''
    frase1=retira_pontuacao(frase)
    frase2=str.lower(frase1)
    frase3=str.split(frase2,' ')
    
    def frase4(h):
        """..."""
        for x in range(len(h)):
            if x< len(h) and h[x] == "":
                del(h[x])
        return h  
      
    frase5=frase4(frase3)
    
    for x in range(len(frase5)):
        x+=1
        fraseinvertida+=frase5[-x]+' '
        
    return str.rstrip(fraseinvertida,' ')