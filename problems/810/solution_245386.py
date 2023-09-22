def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
    msg = list.reverse(frase)
    pontuacao = ('-',',',':',';','.','!','?')
    
#primeiro retirar a pontuação:
    
    if pontuacao in frase:
        msg = str.replace(frase,pontuacao,' ') 
    
    msg = str.lower(frase)
        
    
               
    return msg