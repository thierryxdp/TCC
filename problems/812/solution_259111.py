def retira_pontuacao(frase):
    '''Retira a pontuação de uma frase dada e substitui
       por espaco;
       str -> str'''
    
    for n in frase:
        
        if n == '.' or n == ';' or n == '-' or n == ','
           or n == ':':
                
                n = ' '
    return frase