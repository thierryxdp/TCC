def conta_frases(texto):
    '''
       Função que recebe um texto e conta o número de frases que aparecem nesse texto
       str -> int
    '''
    texto=texto.replace('.','/')
    texto=texto.replace('?','/')
    texto=texto.replace('!','/')
    texto=texto.replace('...','/')
    
    texto=texto.strip('/')
    texto=texto.strip('///')
    texto=texto.replace('///','/')
    
    texto=texto.split('/')
    
    return len(texto)