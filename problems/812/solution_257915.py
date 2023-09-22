def retira_pontuacao (frase):
    '''Função que dada uma frase, retorne a frase ode todos os caracteres de pontuação
    sejam substituidos por espaço. str->str'''
    
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    
    return frase