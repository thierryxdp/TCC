#---------------------EXERCICIO 6---------------------

def lingua_p(texto):
    '''Retorna texto escrito traduzido para lingua p
       str-> str'''
    
    textoTraduzido = ''
    
    for contador in str.lower(texto):
        if contador in 'aàáâãeèéêiìíîoóòôõuùúû':
            textoTraduzido += contador+'p'
        textoTraduzido += contador
        
    return textoTraduzido