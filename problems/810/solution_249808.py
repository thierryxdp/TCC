def inverte(frase):
    '''
    função que recebe uma frase e retorna uma outra frase 
    com os elementos da frase inicial invertidose sem nenhuma
    pontuação ou letras maiúsclas
    
    str -> str
    '''
    um = str.replace(frase,'-',' ')
    dois = str.replace(um,',',' ') 
    tres = str.replace(dois,':',' ')
    quatro = str.replace(tres,';',' ')
    cinco = str.replace(quatro,'.',' ')
    seis = str.replace(cinco,'?',' ')
    sete = str.replace(seis,'!',' ')
    
    final = str.lower(sete)
    
    lista = str.split(final)
    
    invertida = list(reversed(lista))
    
    lista_final = ' '.join(invertida)
    
    return lista_final