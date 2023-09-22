def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma palavra
    traduzida na lingua do P.
    str -> str'''
    
    P_final=''
    
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            P_final+=letra+'p'+letra
        else:
            Pfinal+=letra
    return P_final