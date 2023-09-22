def lingua_p(palavra):
    '''
        Funcao recebe uma palavra em portugues e retorna
        essa palavra traduzida para a lingua do P.
        str -> str
        
    '''
    palavra = palavra.lower()
    traduzida = '' 
    
    for letra in palavra:
        
        if letra in 'aeiouáéíóúãõâêô':
            traduzida = traduzida + letra+'p'+letra
        else:
            traduzida = traduzida + letra
            
    return traduzida