def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma palavra
    traduzida na lingua do P.
    str -> str'''
    
    P_final=''
    
    for letra in palavra:
        if letra in 'AÁEÉIOUaáeéiou':
            P_final+=letra+'p'+letra
        else:
            P_final+=letra
    return P_final