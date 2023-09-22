def lingua_p(palavra):
    
    traduxido_p = []
    contador = 0
    
    for letra in list(palavra):
        if letra in 'abcdef':
            traduzido_p.append(letra + 'p' + letra)
        else:
            traduzido_p.append(letra)
            
    return ''.join(traduzido_p)