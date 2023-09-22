lingua_p(palavra):
    """
    recebe uma palavra e retorna ela na lingua do P
    """
    
    v='AEIOUaeiou'
    P=palavra
    
    for x in palavra:
        if x in v:
            P=palavra[0:x]+'p'+palavra[x:-1]
    return str.lower(P)