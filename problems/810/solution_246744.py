def inverte (frase):
    """Função que, dada uma frase, retorne essa mesma 
    frase onde todos os caracteres de pontuacao tenham
    sido substituidos por espaço."""
    
    b="!@#$%&*().,:-;?":
        for i in range(len (b)):
            frase=frase.replace (b[i]," ")
            texto=frase.lower().split()
            texto.reverse()
            inverti=' '.join(texto)
            return inverti