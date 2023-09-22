def uppCons(frase):
    """ Função que, dados uma """
    
    i = 0
    cons=''
    
    while i < len(frase):
     
        if frase[i] in 'bcnmqwrtypsdfghjlçzxv':
            cons = cons + frase[i]
        i=i + 1
    return cons