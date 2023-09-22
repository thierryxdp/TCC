def retira_pontuacao(frase):
    '''função que, a partir de uma frase pontuada, retorna a frase sem pontuação; str -> str'''
    
    if "." in frase:
        return str.replace(frase, '.',' ')
    
    elif "!" in frase:
        return str.replace(frase, '!',' ')