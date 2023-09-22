def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
    pontuacao = ('-',',',':',';','.','!','?')
    
#primeiro retirar a pontuação:
    
    if pontuacao in frase:
        str.lower(msg)
        msg = str.replace(frase,pontuacao,' ') 
    
    
    str.reverse(lista)
    lista = str.reverse(str.split(msg))
    
    return lista