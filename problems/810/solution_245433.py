def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
    pontuacao = ('-',',',':',';','.','!','?')
    
#primeiro retirar a pontuação:
    
    if pontuacao in frase:
        frase = str.replace(frase,'-',',',':',';','.','!','?',' ') 
    
    return frase

#str.lower(msg)
# str.reverse(lista)
# lista = msg.split()
# str.reverse(lista)