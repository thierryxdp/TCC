def retira_pontuacao(frase):
    """Funcao que retorna uma frase, especificada, sem qualquer tipo de
    pontuação.
    Entrada: str;
    Saida: str;
    
    Parameter:
    frase: Frase que ira perder a pontuação.
    """
    
    frase = frase.replace('.',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace('?',' ')
    
    return frase