def lingua_p(palavra):
    """
    recebe uma palavra e retorna ela na lingua do P
    """
    
    v='AEIOUaeiou'
    P=''
    
    for x in palavra:
        P=P+x
        if x in v:
            P=P+'p'+x
    return str.lower(P)