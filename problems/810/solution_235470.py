def inverte(frase):
    """Funcao que retorna, com base numa frase explicitada anteriormente,
    a mesma frase, so que sem pontuação e toda em minusculo.
    Entrada: str;
    Saida: str;
    
    Entrada:
    frase: Frase para ser modificada
    """
    
    frase = frase.replace('.',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace('?',' ')
    frase = frase.split()
    frase = frase[-1::-1]
    frase = str.join(' ', frase)
    frase = frase.lower()
    
    return frase