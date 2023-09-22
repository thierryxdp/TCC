def retira_pontuacao(frase):
    '''Retira a pontuação de uma frase dada e substitui
       por espaco;
       str -> str'''
    
    nfrase = ''
    
    for n in frase:
        
        if n == '.' or n == ';' or n == '-' or n == ',' or n == ':' or n == '?' or n == '!':
                
                nfrase += ' '
                
        else:
            
            nfrase += n
                
    return nfrase

def inverte(frase):
    '''Retorna uma frase invertida em relação a uma frase
       dada como valor de entrada;
       str -> str'''
    
    nopont = retira_pontuacao(frase)
    minus = nopont.lower()
    palavras = minus.split()
    ind = -1
    invert = []
    
    while ind >= -len(palavras):
        
        invert.append(palavras[ind])
        ind += -1
    
    return str.join(' ',invert)