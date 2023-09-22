def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase
    maiúscula; str -> str'''
    
    b= frase
    i = 0
    consoantes = 'b' and 'c' and 'd' and 'f' and 'g' and 'h' and 'j' and 'k' and 'l' and 'm' and 'n' and 'p' and 'q' and 'r' and 's' and 't' and 'v' and 'w' and 'x' and 'y' and 'z'
    while i < len(frase):
        
        if consoantes in frase[i]:
            b = consoantes.upper()
                                
        i=i+1
        
    return b