def retira_pontuacao(frase):
    '''Retira a pontuação de uma frase dada e substitui
       por espaco;
       str -> str'''
    
    ind = 0
    
    for n in frase:
        
        if n == '.' or n == ';' or n == '-' or n == ',' or n == ':':
                
                frase[ind] = ' '
               
        ind += 1
                
    return frase