retira_pontuacao(frase):
    
    for dado in frase:
        
        if dado == '-' or dado == '.' or dado = ',' or dado == '!' or dado = '?':
            
            frase.replace(dado, ' ')
            
    return frase