def lingua_p(palavrinha):
    '''a seguinte função irá receber uma palavra em
    português e irá retornar a mesma traduzida na
    língua do p. str--> str'''
    
    traduzido_p = []  
    contador = 0  

    for letras in list(palavrinha):
        if letras in 'áéíóúaeiou':
            traduzido_p.append(letras + 'p' + letras) 
        else:
            traduzido_p.append(letras)

    return ''.join(traduzido_p)