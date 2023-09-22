def lingua_p(palavra):
    """
    recebe uma palavra e retorna ela na lingua do P
    """
    
    v='AEIOUaeiou'
    P=palavra
    i=0
    
    for x in palavra:
        if x in v:
            P=palavra[0:i]+'p'+palavra[i:-1]
        i+=1
    return str.lower(P)