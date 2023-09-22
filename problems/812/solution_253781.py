def retira_pontuacao(frase):
    '''função que, a partir de uma frase pontuada, retorna a frase sem pontuação; str -> str'''
    
    if "." in frase and("!" and "," and "?" and ":" and "-" and ";") not in frase:
        return str.replace(frase, '.',' ')
    
    elif "!" in frase and("." and ";" and "?" and "-" and ":" and ",") not in frase:
        return str.replace(frase, '!',' ')
    
    elif "?" in frase and ("." and ";" and "!" and "-" and ":" and ",") not in frase:
        return str.replace(frase, '?', ' ')
    
    elif "." and "," and "-"in frase:
        return str.replace(frase, '.', ' ') and str.replace(frase, ',', ' ') and str.replace(frase, '-', ' ')
    
    elif "," and "?" in frase:
        return str.replace(frase, ',', ' ') and str.replace(frase, '?', ' ')