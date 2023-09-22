def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
    pontuacao = ('-',',',':',';','.','!','?')
    
#primeiro retirar a pontuação:
    
    if pontuacao in frase:
        str.lower(msg)
        msg = str.replace(frase,('-',',',':',';','.','!','?'),' ') 
    
    return msg

# str.reverse(lista)
# lista = msg.split()
# str.reverse(lista)