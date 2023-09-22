def lingua_p(palavrinha):
    '''função que recebe palavra em português e
    retorna palavra traduzida em língua do p.
    str--> str'''
    
    traduzido_p = []  
    contador = 0  

    for letra in list(palavrinha):
        if letra in 'áéíóúaeiou':
            traduzido_p.append(letras + 'p' + letras) 
        else:
            traduzido_p.append(letras)

    return ''.join(traduzido_p)