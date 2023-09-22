def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação foram susbstituídos por espaço
    str->str'''
    
    ponto=str.replace(frase,'.',' ',(str.count(frase,'.',)))
    
    return ponto