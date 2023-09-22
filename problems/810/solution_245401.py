def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
    msg = str.reverse(frase)
    pontuacao = ('-',',',':',';','.','!','?')
    
#primeiro retirar a pontuação:
    
    if pontuacao in frase:
        msg = str.replace(frase,pontuacao,' ') 
    
    str.lower(msg)
    str.reverse(msg)
    lista = msg.split()
    
    return lista