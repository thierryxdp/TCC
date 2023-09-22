def inverte(frase):
    """Função que, dada uma frase, retorne essa mesma fras
    onde todos os caracteres de pontuacao tenham sido 
    substituidos por espaço."""
    b="!@#$%&*()., :-;?"
    for i in b:
        frase = frase.replace(i, ' ')
        
    texto.reverse(frase)
    return frase