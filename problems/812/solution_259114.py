def retira_pontuacao(frase):
    '''Retira a pontuação de uma frase dada e substitui
       por espaco;
       str -> str'''
    
    nfrase = ''
    
    for n in frase:
        
        if n == '.' or n == ';' or n == '-' or n == ',' or n == ':':
                
                nfrase.append(' ')
                
        else:
            
            nfrase.append(n)
                
    return nfrase