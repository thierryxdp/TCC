def substitui(frase):
    """Função que, dada uma frase, irá retornar a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço.
    
    	Parameters:
        frase: frase que deverá ter suas pontuações substituídas por um espaço.   
    """

    return str.replace(frase, "." "!" "?", " ")